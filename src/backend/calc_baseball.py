def __round2(value: float, d:int = 3) -> float:
    return round(value, d)

def __base_points(single, double, triple, HR):
    total_points = (single + double * 2 + triple * 3 + HR * 4)
    return total_points


def calc_obp(H, BB, GP, VB, SH):
    OBP = (H + BB + GP) / (VB + BB + GP - SH)
    OBP = __round2(OBP)
    return OBP

def calc_slg(VB, single, double, triple, HR):
    bases = __base_points(single, double, triple, HR)
    SLG = bases / VB
    SLG = __round2(SLG)
    return SLG
    
def calc_ops(H, BB, GP, VB, SH, single, double, triple, HR):
    OBP = calc_obp(H, BB, GP, VB, SH)
    SLG = calc_slg(VB, single, double, triple, HR)
    OPS = OBP + SLG
    OPS = __round2(OPS)
    return OPS
    
def calc_k9(K, IP):
    K9 = (K / IP) * 9
    K9 = __round2(K9)
    return K9
    
def calc_fip(HR, BB, GP, IBB, K, IP):
    FIP = (HR * 13 + (BB + GP - IBB) * 3 - K * 2) / IP
    FIP = __round2(FIP)
    return FIP

def calc_babip(H, HR, K, SF, TB):
    VB = TB - K - HR
    BABIP = (H - HR) / (VB - HR - K + SF)
    BABIP = __round2(BABIP)
    return BABIP
