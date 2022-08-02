from django.contrib import admin

from settlement.models import BedFee, CUUsage, DiagFee, DiagInfo, ExamFee, GeneralDiagFee, LabTestFee, MainDiag, MainDisease, MainOp, MedMaterialFee, NursingFee, OpFee, OtherDiag, OtherFee, OtherOp, MainSymp, RegistrationFee, Settlement, PostAdmitComa, PreAdmitComa, SpecialFee, TotalFee, TraditionalPatentFee, TraditionalRelease, TraditionalTabletFee, Transfusion, TreatFee, VentilatorDuration, WesternMedFee, WesternRelease

# Register your models here.
admin.site.register(Settlement)
admin.site.register(VentilatorDuration)
admin.site.register(PreAdmitComa)
admin.site.register(PostAdmitComa)
admin.site.register(MainOp)
admin.site.register(OtherOp)
admin.site.register(DiagInfo)
admin.site.register(WesternRelease)
admin.site.register(TraditionalRelease)
admin.site.register(MainDiag)
admin.site.register(OtherDiag)
admin.site.register(MainDisease)
admin.site.register(MainSymp)
admin.site.register(CUUsage)
admin.site.register(Transfusion)
admin.site.register(BedFee)
admin.site.register(DiagFee)
admin.site.register(ExamFee)
admin.site.register(LabTestFee)
admin.site.register(TreatFee)
admin.site.register(OpFee)
admin.site.register(NursingFee)
admin.site.register(MedMaterialFee)
admin.site.register(WesternMedFee)
admin.site.register(TraditionalTabletFee)
admin.site.register(TraditionalPatentFee)
admin.site.register(GeneralDiagFee)
admin.site.register(RegistrationFee)
admin.site.register(OtherFee)
admin.site.register(SpecialFee)
admin.site.register(TotalFee)