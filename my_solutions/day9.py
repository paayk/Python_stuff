# ================= Q26 =======================
print('=================== Q26 ===================')

def sum_of_two(a,b):
    return a + b
# lambda way :  ==>  sum = lambda n1, n2: n1 + n2
print(sum_of_two(10, 11))
# ================ DONE =======================

# ============ Q27 ==============================
print('===================== Q27 ===================')
to_str = lambda num: str(num)
print(type(to_str(1)))

# =============== DONE ===========================

#  ================== Q28 ========================
print('==================== Q28 ================')
sum_of_str = lambda num, num2: int(num) + int(num2)
print(sum_of_str('4', '5'))
# ================= DONE ==================

#  ================ Q29 ======================
print('=================== Q29 ====================')
conc_str = lambda s1, s2: s1 + s2
print(conc_str('haha', 'hihi'))
# ============== DONE ======================

# ============= Q30 ===============================
print('================ Q30 ===================')

l1 = 0
l2 = 0
def print_len(s1, s2):
    if len(s1) > len(s2):
        return s1
    elif len(s1) == len(s2):
        return '{0}\n{1}'.format(s1, s2)
    return s2
s1, s2 = input('> the spliter is | : ').split('|')
print(print_len(s1, s2))
# ===================== DONE ========================= 