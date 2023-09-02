from django.db import models

# Create your models here.
class Quote(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    business_name = models.CharField(max_length=50, blank=True, null=True)
    contact_name = models.CharField(max_length=50)
    notes = models.TextField(max_length=1000, blank=True, null=True)
    brazed = models.BooleanField(default=False)
    surface_area = models.IntegerField(default=0)
    electroless = models.BooleanField(default=False)
    particle = models.CharField(max_length=20, default='synthetic', choices=[
        ("synthetic", "Synthetic"),
        ("natural", "Natural"),
        ("blend", "Blend"),
        ("cbn", "CBN"),
    ])
    grit = models.CharField(max_length=7, blank=True, null=True, choices=[
        ("16/18", "16/18"),
        ("18/20", "18/20"),
        ("20/30", "20/30"),
        ("30/40", "30/40"),
        ("40/50", "40/50"),
        ("50/60", "50/60"),
        ("60/80", "60/80"),
        ("80/100", "80/100"),
        ("80/120", "80/120"),
        ("100/120", "100/120"),
        ("120/140", "120/140"),
        ("140/170", "140/170"),
        ("170/200", "170/200"),
        ("200/230", "200/230"),
        ("230/270", "230/270"),
        ("270/325", "270/325"),
        ("325/400", "325/400"),
        ("400", "400"),
        ("500", "500"),
        ("600", "600"),
        ("800", "800"),
        ("1200", "1200"),
        ("1500", "1500"),
        ("2000", "2000")
    ])
    fixture = models.BooleanField(default=False)
    fixture_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tooling_type = models.CharField(max_length=20, default="customerProvided", choices=[
        ("customerProvided", "Customer Provided"),
        ("stripReplate", "Strip & Replate"),
        ("blankNeeded", "Blank Needed"),
    ]),
    strip_replate = models.CharField(max_length=25, blank=True, null=True, choices=[
        ("small/easy part", "Small/Easy Part"),
        ("medium size/difficulty", "Medium Size/Difficulty"),
        ("large/difficult part", "Large/Difficult Part"),
    ])
    blank_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    machining = models.BooleanField(default=False)
    machine_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    prep_labor = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    plating_labor = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    cleaning_labor = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    pack_labor = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    difficulty = models.CharField(max_length=20, choices=[
        ("easy", "Easy"),
        ("moreDifficult", "More Difficult"),
        ("veryDifficult", "Very Difficult")
    ])
    expedited = models.BooleanField(default=False)

