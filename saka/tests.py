from django.test import TestCase

# Create your tests here.

## Change every Entry so that it belongs to this Blog.
# Question.objects.all().update(question_text=b)

# def test(request):
#     if request.method == 'POST':
#         form = forms.Cash_form(request.POST)
#         if form.is_valid():
#             value = form.save(commit=False)
#             obj_cash = models.Cash.objects.filter(laboratoryid=value.laboratoryid).filter(analyteid=value.analyteid).filter(department=value.department)
#             obj_cash.update(kittype=value.kittype,
#                             testmethod=value.testmethod,
#                             devicetype=value.devicetype,
#                             latnumber=value.latnumber,
#                             analytecv=value.analytecv,
#                             testresult=value.testresult)
#             print(obj_cash)
#             return redirect('saka:test')
#         else:
#             print('not valid')
#     else:
#         form = forms.Cash_form()
#     return render(request, 'saka/test.html', {'form': form})


# {'csrfmiddlewaretoken': ['2QSXn8g07jEfQeJO5OE6o8RZiA8gSjY5rHsohSLu5HrNBI4GNH4ikR43J9483mxB'], 'latnumber': ['31'],
#  'Glucose': ['273.0'], 'cvglucose': ['3.58'], 'devicetypeglucose': ['1'], 'testmethodglucose': ['1'],
#  'kittypeglucose': ['1'], 'BUN': [''], 'cvbun': [''], 'devicetypebun': ['...'], 'testmethodbun': ['...'],
#  'kittypebun': ['...'], 'Creatinine': ['4.22'], 'cvcreatinine': ['3.86'], 'devicetypecreatinine': ['3'],
#  'testmethodcreatinine': ['3'], 'kittypecreatinine': ['3'], 'Triglyceride': ['97.0'], 'cvtriglyceride': ['3.18'],
#  'devicetypetriglyceride': ['4'], 'testmethodtriglyceride': ['4'], 'kittypetriglyceride': ['4'],
#  'Cholesterol': ['107.0'], 'cvcholesterol': ['2.2'], 'devicetypecholesterol': ['5'], 'testmethodcholesterol': ['5'],
#  'kittypecholesterol': ['5'], 'Uricacid': ['7.6'], 'cvuricacid': ['4.33'], 'devicetypeuricacid': ['6'],
#  'testmethoduricacid': ['6'], 'kittypeuricacid': ['6'], 'LDL': [''], 'cvldl': [''], 'devicetypeldl': ['...'],
#  'testmethodldl': ['...'], 'kittypeldl': ['...'], 'HDL': ['26.0'], 'cvhdl': ['2.18'], 'devicetypehdl': ['8'],
#  'testmethodhdl': ['8'], 'kittypehdl': ['8'], 'TBili': ['4.27'], 'cvtbili': ['2.11'], 'devicetypetbili': ['9'],
#  'testmethodtbili': ['9'], 'kittypetbili': ['9'], 'DBili': ['0.99'], 'cvdbili': ['3.73'], 'devicetypedbili': ['10'],
#  'testmethoddbili': ['10'], 'kittypedbili': ['...'], 'Albumin': ['2.6'], 'cvalbumin': ['3.27'],
#  'devicetypealbumin': ['11'], 'testmethodalbumin': ['11'], 'kittypealbumin': ['...'], 'TotalProtein': ['4.4'],
#  'cvtotalprotein': ['2.66'], 'devicetypetotalprotein': ['12'], 'testmethodtotalprotein': ['12'],
#  'kittypetotalprotein': ['...'], 'SGOT': ['156.0'], 'cvsgot': ['2.56'], 'devicetypesgot': ['13'],
#  'testmethodsgot': ['13'], 'kittypesgot': ['...'], 'SGPT': ['84.0'], 'cvsgpt': ['3.47'], 'devicetypesgpt': ['14'],
#  'testmethodsgpt': ['...'], 'kittypesgpt': ['...'], 'ALK': ['428.0'], 'cvalk': ['2.5'], 'devicetypealk': ['15'],
#  'testmethodalk': ['15'], 'kittypealk': ['...'], 'CPK': [''], 'cvcpk': [''], 'devicetypecpk': ['...'],
#  'testmethodcpk': ['...'], 'kittypecpk': ['...'], 'LDH': ['785.0'], 'cvldh': ['2.19'], 'devicetypeldh': ['17'],
#  'testmethodldh': ['17'], 'kittypeldh': ['...'], 'Amylase': [''], 'cvamylase': [''], 'devicetypeamylase': ['...'],
#  'testmethodamylase': ['...'], 'kittypeamylase': ['...'], 'Calcium': ['11.3'], 'cvcalcium': ['2.39'],
#  'devicetypecalcium': ['19'], 'testmethodcalcium': ['19'], 'kittypecalcium': ['...'], 'Phosphorus': ['6.6'],
#  'cvphosphorus': ['3.16'], 'devicetypephosphorus': ['20'], 'testmethodphosphorus': ['20'], 'kittypephosphorus': ['...'],
#  'Iron': ['88.0'], 'cviron': ['3.98'], 'devicetypeiron': ['21'], 'testmethodiron': ['21'], 'kittypeiron': ['...'],
#  'TIBC': [''], 'cvtibc': [''], 'devicetypetibc': ['...'], 'testmethodtibc': ['...'], 'kittypetibc': ['...'],
#  'Sodium': [''], 'cvsodium': [''], 'devicetypesodium': ['...'], 'testmethodsodium': ['...'], 'kittypesodium': ['...'],
#  'Potassium': [''], 'cvpotassium': [''], 'devicetypepotassium': ['...'], 'testmethodpotassium': ['...'],
#  'kittypepotassium': ['...'], 'Lipase': [''], 'cvlipase': [''], 'devicetypelipase': ['...'],
#  'testmethodlipase': ['...'], 'kittypelipase': ['...'], 'CRP': [''], 'cvcrp': [''], 'devicetypecrp': ['...'],
#  'testmethodcrp': ['...'], 'kittypecrp': ['...'], 'button_1': ['ذخیره موقت']} >
