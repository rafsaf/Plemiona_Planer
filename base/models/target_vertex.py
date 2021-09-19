from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy


class TargetVertex(models.Model):
    """Target Village"""

    MODE_OFF = [
        ("closest", gettext_lazy("Closest Front")),
        ("close", gettext_lazy("Close Back")),
        ("random", gettext_lazy("Random Back")),
        ("far", gettext_lazy("Far Back")),
    ]

    MODE_NOBLE = [
        ("closest", gettext_lazy("Closest Front")),
        ("close", gettext_lazy("Close Back")),
        ("random", gettext_lazy("Random Back")),
        ("far", gettext_lazy("Far Back")),
    ]

    MODE_DIVISION = [
        ("divide", gettext_lazy("Divide off with nobles")),
        ("not_divide", gettext_lazy("Dont't divide off")),
        ("separatly", gettext_lazy("Off and nobles separatly")),
    ]

    NOBLE_GUIDELINES = [
        ("one", gettext_lazy("Try send all nobles to one target")),
        ("many", gettext_lazy("Nobles to one or many targets")),
        ("single", gettext_lazy("Try single nobles from many villages")),
    ]

    outline = models.ForeignKey("Outline", on_delete=models.CASCADE, db_index=True)
    outline_time = models.ForeignKey(
        "OutlineTime", on_delete=models.SET_NULL, null=True, default=None
    )
    target = models.CharField(max_length=7, db_index=True)
    player = models.CharField(max_length=30)
    fake = models.BooleanField(default=False)
    ruin = models.BooleanField(default=False)

    required_off = models.IntegerField(default=0)
    required_noble = models.IntegerField(default=0)

    exact_off = ArrayField(models.IntegerField(), default=list, size=4)
    exact_noble = ArrayField(models.IntegerField(), default=list, size=4)

    mode_off = models.CharField(max_length=15, choices=MODE_OFF, default="random")
    mode_noble = models.CharField(max_length=15, choices=MODE_NOBLE, default="closest")
    mode_division = models.CharField(
        max_length=15, choices=MODE_DIVISION, default="not_divide"
    )
    mode_guide = models.CharField(
        max_length=15, choices=NOBLE_GUIDELINES, default="one"
    )
    night_bonus = models.BooleanField(default=False)
    enter_t1 = models.IntegerField(default=7)
    enter_t2 = models.IntegerField(default=12)

    def __str__(self):
        return self.target

    def get_absolute_url(self):
        return reverse("base:planer_initial_detail", args=[self.outline.pk, self.pk])

    def coord_tuple(self):
        return (int(self.target[0:3]), int(self.target[4:7]))
