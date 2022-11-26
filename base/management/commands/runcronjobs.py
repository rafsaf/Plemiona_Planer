# Copyright 2022 Rafał Safin (rafsaf). All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


import logging
import time

import schedule
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

import metrics
from base.management.commands.utils import run_threaded

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Cronjobs runner"

    def handle(self, *args, **options):
        log.info("task runcronjobs start")
        try:
            schedule.every(settings.JOB_MIN_INTERVAL).to(
                settings.JOB_MAX_INTERVAL
            ).minutes.do(run_threaded, call_command, command_name="dbupdate")
            schedule.every().hour.do(
                run_threaded, call_command, command_name="outdateoverviewsdelete"
            )
            schedule.every().hour.do(
                run_threaded, call_command, command_name="outdateoutlinedelete"
            )
            schedule.every(5).minutes.do(
                run_threaded, call_command, command_name="calculatepaymentfee"
            )
            schedule.every(15).seconds.do(
                run_threaded, call_command, command_name="hostparameters"
            )
            schedule.every(60).to(120).seconds.do(
                run_threaded, call_command, command_name="worldlastupdate"
            )

            call_command("dbupdate")  # extra db_update on startup

            secs_lifetime: int = settings.JOB_LIFETIME_MAX_SECS
            rounds = secs_lifetime / 5
            while True:
                schedule.run_pending()
                time.sleep(5)
                if secs_lifetime:
                    if rounds < 0:
                        break
                    rounds -= 1

            log.info("Cronjobs restarting in 60s...")
            time.sleep(60)  # grace period 60s waiting for threads end
        except Exception as error:
            msg = f"task runcronjobs failed: {error}"
            self.stdout.write(self.style.ERROR(msg))
            log.error(msg)
            metrics.ERRORS.labels("task_runcronjobs").inc()
