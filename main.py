from src.Diagrams import *

a1 = BB_TEL10(name='A1')
a2=PS7('A2')
a3=BU_TEL('A3')
a4=BP_TEL('A4')
a5=MR500_V2('A5')
a6=PS3_old('A6')
a8=DUGA_O('A8')
a9=PS12('A9')
kv1=R3('KV1', highlight=True)
kv2=R3('KV2')
kv3=R3('KV3')
pa=CP8501_14('PA')
pik=CC301('PIK')
r1=R('R1', highlight=True)
r2=R('R2')
r3=R('R3')
r4=R('R4')
r5=R('R5')
r6=R('R6')
r7=R('R7')
r8=R('R8')
r9=R('R9')
r10=R('R10')
r11=R('R11')
r12=R('R12')
r13=R('R13')
r14=R('R14')
r15=R('R15')
r16=R('R16')
r17=R('R17')
r18=R('R18')
sb1=SB_F('SB1')
sb2=SB_F('SB2')
sf1=SF2('SF1')
sf2=SF2('SF2')
sg1=BI4('SG1')
sg2=BI6('SG2')
sg3=BI4('SG3')
sx1=AC22_old('SX1',highlight=True)
sx2=AC22_old('SX2')
sx3=AC22_old('SX3')
sx4=AC22_old('SX4')
sx5=AC22_old('SX5')
sx6=AC22_old('SX6')
ct_a = CT3('TA-A')
ct_b = CT3('TA-B')
ct_c = CT3('TA-C')
x = Connectors('X', 30)
xt1 = XT('XT1', 120)
xt2 = XT('XT2', 70)
xt3 = XT('XT3', 32, 'СШР55-П30-ЗГ1')

#Выкатной элемент
v_e = [a1, x]
#Дверь релейного отсека
d_r_o = [a2,a5,a6,a8,a9,pa,pik,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,sb1,sb2,sx1,sx2,sx3,sx4,sx5,sx6,xt3]
#Шасси релейного отсека
sh_r_o = [a3,a4,kv1,kv2,kv3,r1,r2,sf1,sf2,sg1,sg2,sg3,xt2]
#Отсек трансформаторов тока
o_tt = [ct_a,ct_b,ct_c]
#Релейный отсек
r_o = [x,xt1]
all_list = v_e+d_r_o+sh_r_o+o_tt+r_o
d = {}
for i in all_list:
	d[i.name] = i

w = []
w.append(Wire(a4,5,a4,6))
w.append(Wire(a4,5,a3,2))
w.append(Wire(a4,8,a4,9))
w.append(Wire(a4,8,a3,1))
w.append(Wire(a4,11,xt1,23))
w.append(Wire(a4,12,xt1,24))
w.append(Wire(a4,14,xt2,14))
w.append(Wire(a4,15,xt2,1))
w.append(Wire(a4,16,xt2,24))
w.append(Wire(a4,18,a2,13))
w.append(Wire(a3,3,xt2,36))
w.append(Wire(a3,4,xt2,37))
w.append(Wire(a3,5,xt2,38))
w.append(Wire(a3,6,xt2,39))
w.append(Wire(a3,7,xt2,17))
w.append(Wire(a3,8,xt2,40))
w.append(Wire(a3,9,xt2,19))
w.append(Wire(a3,10,sg2,2))
w.append(Wire(a3,11,a5,'X6:1'))
w.append(Wire(a3,12,sg2,6))
w.append(Wire(a3,13,a5,'X6:7'))
w.append(Wire(r1,1,xt1,9))
w.append(Wire(r1,2,r2,1))
w.append(Wire(r2,2,sx5,1))
w.append(Wire(kv1,'A',xt2,22))
w.append(Wire(kv1,'B',kv2,'B'))
w.append(Wire(kv1,11,xt2,17))
w.append(Wire(kv1,11,kv2,11))
w.append(Wire(kv1,14,xt2,40))
w.append(Wire(kv2,'A',xt2,23))
w.append(Wire(kv2,'B',xt2,15))
w.append(Wire(kv2,14,xt2,19))
w.append(Wire(kv3,'A',a8,2))
w.append(Wire(kv3,'B',xt1,14))
w.append(Wire(kv3,11,xt2,5))
w.append(Wire(kv3,12,sx1,1))
w.append(Wire(kv3,14,sx2,1))
w.append(Wire(kv3,21,xt1,15))
w.append(Wire(kv3,24,xt1,16))
w.append(Wire(kv3,31,xt1,17))
w.append(Wire(kv3,34,xt1,18))
w.append(Wire(sf1,1,xt1,1))
w.append(Wire(sf1,2,xt2,1))
w.append(Wire(sf1,3,xt1,2))
w.append(Wire(sf1,4,xt2,14))
w.append(Wire(sf2,1,xt1,11))
w.append(Wire(sf2,2,xt2,24))
w.append(Wire(sf2,3,xt1,12))
w.append(Wire(sf2,4,xt2,52))
w.append(Wire(sg1,1,ct_a,'1И1'))
w.append(Wire(sg1,3,ct_b,'1И1'))
w.append(Wire(sg1,5,ct_c,'1И1'))
w.append(Wire(sg1,7,ct_c,'1И2'))
w.append(Wire(sg1,2,pa,1))
w.append(Wire(sg1,4,pik,4))
w.append(Wire(sg1,6,pik,7))
w.append(Wire(sg1,8,pik,3))
w.append(Wire(sg2,1,ct_a,'2И1'))
w.append(Wire(sg2,3,ct_b,'2И1'))
w.append(Wire(sg2,5,ct_c,'2И1'))
w.append(Wire(sg2,7,ct_c,'2И2'))
w.append(Wire(sg2,2,a3,10))
w.append(Wire(sg2,4,a5,'X6:4'))
w.append(Wire(sg2,6,a3,12))
w.append(Wire(sg2,8,a5,'X6:2'))
w.append(Wire(pa,14,xt1,51))
w.append(Wire(pa,2,pik,1))
w.append(Wire(pa,4,xt2,26))
w.append(Wire(pa,5,xt2,53))
w.append(Wire(pa,13,xt1,50))
w.append(Wire(a9,'1',a9,'2'))
w.append(Wire(a9,'3',a9,'2'))
w.append(Wire(a9,'3',a9,'4'))
w.append(Wire(a9,'4',a9,'5'))
w.append(Wire(a9,'5',a9,'6'))
w.append(Wire(a9,'6',a9,'13'))
w.append(Wire(a9,'13',a9,'14'))
w.append(Wire(a9,'14',xt2,54))
w.append(Wire(a9,'1h',xt2,56))
w.append(Wire(a9,'2h',xt2,57))
w.append(Wire(a9,'3h',xt2,58))
w.append(Wire(a9,'4h',xt2,59))
w.append(Wire(a9,'5h',xt2,60))
w.append(Wire(a9,'6h',xt2,61))
w.append(Wire(a9,'13h',sx6,2))
w.append(Wire(a9,'14h',xt2,27))
w.append(Wire(a2,1,xt2,52))
w.append(Wire(a2,2,xt2,25))
w.append(Wire(a2,2,a2,10))
w.append(Wire(a2,10,a2,12))
w.append(Wire(a2,12,a2,14))
w.append(Wire(a2,14,a2,16))
w.append(Wire(a2,16,a2,18))
w.append(Wire(a2,3,xt1,113))
w.append(Wire(a2,4,xt1,114))
w.append(Wire(a2,9,a6,14))
w.append(Wire(a2,11,a8,12))
w.append(Wire(a2,15,a5,'X7:4'))
w.append(Wire(a2,17,a5,'X2:2'))
w.append(Wire(a6,5,xt2,26))
w.append(Wire(a6,6,xt2,53))
w.append(Wire(a6,7,xt2,46))
w.append(Wire(a6,8,xt2,47))
w.append(Wire(a6,9,xt2,48))
w.append(Wire(a6,10,xt2,49))
w.append(Wire(a6,11,xt2,50))
w.append(Wire(a6,12,xt2,51))
w.append(Wire(a6,13,a6,5))
w.append(Wire(a8,1,xt1,13))
w.append(Wire(a8,1,a8,3))
w.append(Wire(a8,5,a8,3))
w.append(Wire(a8,2,a8,4))
w.append(Wire(a8,4,a8,6))
w.append(Wire(a8,11,a8,14))
w.append(Wire(a8,13,xt2,53))
w.append(Wire(a8,14,xt2,26))
w.append(Wire(a5,'X2:1',a5,'X7:3'))
w.append(Wire(a5,'X2:1',xt2,24))
w.append(Wire(a5,'X2:3',xt2,18))
w.append(Wire(a5,'X2:4',xt2,41))
w.append(Wire(a5,'X2:5',xt2,17))
w.append(Wire(a5,'X2:6',xt2,20))
w.append(Wire(a5,'X1:2',xt2,4))
w.append(Wire(a5,'X1:3',xt2,16))
w.append(Wire(a5,'X6:2',a5,'X6:5'))
w.append(Wire(a5,'X6:8',a5,'X6:5'))
w.append(Wire(a5,'X7:1',xt2,18))
w.append(Wire(a5,'X7:2',xt2,41))
w.append(Wire(a5,'X7:5',xt1,55))
w.append(Wire(a5,'X7:6',xt1,56))
w.append(Wire(a5,'X7:7',xt1,57))
w.append(Wire(a5,'X7:8',xt1,58))
w.append(Wire(a5,'X7:9',x,'p8'))
w.append(Wire(a5,'X7:10',xt1,64))
w.append(Wire(a5,'X7:11',xt2,42))
w.append(Wire(a5,'X7:12',xt2,43))
w.append(Wire(a5,'X7:13',xt2,44))
w.append(Wire(a5,'X7:14',xt2,45))
w.append(Wire(a5,'X7:15',xt2,18))
w.append(Wire(a5,'X7:16',xt2,20))
w.append(Wire(a5,'X8:1',xt3,1))
w.append(Wire(a5,'X8:2',xt3,2))
w.append(Wire(a5,'X8:3',xt3,3))
w.append(Wire(a5,'X8:4',xt3,4))
w.append(Wire(a5,'X8:5',xt3,5))
w.append(Wire(a5,'X8:6',xt3,6))
w.append(Wire(a5,'X8:7',xt3,7))
w.append(Wire(a5,'X8:8',xt3,8))
w.append(Wire(a5,'X8:9',xt3,9))
w.append(Wire(a5,'X8:10',xt3,10))
w.append(Wire(a5,'X8:11',xt3,11))
w.append(Wire(a5,'X8:12',xt3,12))
w.append(Wire(a5,'X8:13',xt3,13))
w.append(Wire(a5,'X8:14',xt3,14))
w.append(Wire(a5,'X8:15',xt3,15))
w.append(Wire(a5,'X8:16',xt3,16))
w.append(Wire(a5,'X9:1',xt3,17))
w.append(Wire(a5,'X9:2',xt3,18))
w.append(Wire(a5,'X9:3',xt3,19))
w.append(Wire(a5,'X9:4',xt3,20))
w.append(Wire(a5,'X9:5',xt3,21))
w.append(Wire(a5,'X9:6',xt3,22))
w.append(Wire(a5,'X9:7',xt3,23))
w.append(Wire(a5,'X9:8',xt3,24))
w.append(Wire(a5,'X9:9',xt3,25))
w.append(Wire(a5,'X9:10',xt3,26))
w.append(Wire(a5,'X9:11',xt3,27))
w.append(Wire(a5,'X9:12',xt3,28))
w.append(Wire(a5,'X9:13',xt3,29))
w.append(Wire(a5,'X9:14',xt3,30))
w.append(Wire(a5,'X9:15',xt3,31))
w.append(Wire(a5,'X9:16',xt3,32))
w.append(Wire(pik,2,xt2,31))
w.append(Wire(pik,5,xt2,32))
w.append(Wire(pik,8,xt2,33))
w.append(Wire(pik,11,xt2,34))
w.append(Wire(pik,3,pik,6))
w.append(Wire(pik,9,pik,6))
w.append(Wire(sb1,13,xt2,5))
w.append(Wire(sb1,14,xt3,5))
w.append(Wire(sb1,13,sb2,13))
w.append(Wire(sb2,14,xt3,7))
w.append(Wire(sb1,'X1',x,'s2'))
w.append(Wire(sb1,'X2',xt2,52))
w.append(Wire(sb1,'X2',sb2,'X2'))
w.append(Wire(sb2,'X1',x,'s18'))
w.append(Wire(sx1,2,xt3,9))
w.append(Wire(sx2,2,xt3,11))
w.append(Wire(sx3,1,xt2,6))
w.append(Wire(sx3,2,xt3,13))
w.append(Wire(sx4,1,xt1,71))
w.append(Wire(sx4,2,xt3,31))
w.append(Wire(sx5,2,xt1,10))
w.append(Wire(sx6,1,xt2,27))
w.append(Wire(r3,1,xt3,1))
w.append(Wire(r3,2,xt3,2))
w.append(Wire(r4,1,xt3,3))
w.append(Wire(r4,2,xt3,4))
w.append(Wire(r5,1,xt3,5))
w.append(Wire(r5,2,xt3,6))
w.append(Wire(r6,1,xt3,7))
w.append(Wire(r6,2,xt3,8))
w.append(Wire(r7,1,xt3,9))
w.append(Wire(r7,2,xt3,10))
w.append(Wire(r8,1,xt3,11))
w.append(Wire(r8,2,xt3,12))
w.append(Wire(r9,1,xt3,13))
w.append(Wire(r9,2,xt3,14))
w.append(Wire(r10,1,xt3,15))
w.append(Wire(r10,2,xt3,16))
w.append(Wire(r11,1,xt3,17))
w.append(Wire(r11,2,xt3,18))
w.append(Wire(r12,1,xt3,19))
w.append(Wire(r12,2,xt3,20))
w.append(Wire(r13,1,xt3,21))
w.append(Wire(r13,2,xt3,22))
w.append(Wire(r14,1,xt3,23))
w.append(Wire(r14,2,xt3,24))
w.append(Wire(r15,1,xt3,25))
w.append(Wire(r15,2,xt3,26))
w.append(Wire(r16,1,xt3,27))
w.append(Wire(r16,2,xt3,28))
w.append(Wire(r17,1,xt3,29))
w.append(Wire(r17,2,xt3,30))
w.append(Wire(r18,1,xt3,31))
w.append(Wire(r18,2,xt3,32))
w.append(Wire(ct_a,'1И2',ct_b,'1И2'))
w.append(Wire(ct_a,'2И2',ct_b,'2И2'))
w.append(Wire(ct_a,'3И1',sg3,1))
w.append(Wire(ct_a,'3И2',ct_b,'3И2'))
w.append(Wire(ct_b,'1И2',ct_c,'1И2'))
w.append(Wire(ct_b,'2И2',ct_c,'2И2'))
w.append(Wire(ct_b,'3И1',sg3,3))
w.append(Wire(ct_b,'3И2',ct_c,'3И2'))
w.append(Wire(ct_c,'3И1',sg3,5))
w.append(Wire(ct_c,'3И2',sg3,7))


cd = CircuitDiagram('Оперативные цепи', w, d)
cd.place_elements()


# doc2 = ezdxf.new()
# doc2.units = ezdxf.units.MM
# msp2 = doc2.modelspace()
# list_elements = [[a3,[100,0]],
#                  [a4, [30,0]],
#                  [kv1,[30,-200]],
#                  [kv2,[100,-200]],
#                  [kv3, [170, -200]],
#                  [sf1, [50,-280]],
#                  [sf2, [120, -280]],
#                  [r1,[50,-350]],
#                  [r2, [100, -350]],
#                  [sg1,[0,-400]],
#                  [sg2,[70,-400]],
#                  [sg3,[170,-400]],
#                  [xt2,[-50,0]]]
#
#
#
# WiringDiagram(list_elements, w, msp2)
# doc2.saveas("Монтажная схема шасси релейного отсека.dxf", encoding='utf-8')
#
# doc3 = ezdxf.new()
# doc3.units = ezdxf.units.MM
# msp3 = doc3.modelspace()
# list_elements = [ [a2,[30,70]],
#                   [a5, [-70,-140]],
#                   [a6, [80,0]],
#                   [a8, [0,0]],
#                   [a9, [-20,-100]],
#                   [pa,[0,-280]],
#                  [pik, [ 0,-160]],
#                 [sx1,[0,-200]],
#                 [sx3,[60,-200]],
#                 [sx5,[120,-200]],
#                 [sx2,[0,-230]],
#                 [sx4,[60,-230]],
#                 [sx6,[120,-230]],
#                  [sb1,[180,-180]],
#                  [sb2,[180,-230]],
#                   [r3,[150,30]],
#                   [r4, [150, 20]],
#                   [r5, [150, 10]],
#                   [r6, [150, 0]],
#                   [r7, [150, -10]],
#                   [r8, [150, -20]],
#                   [r9, [150, -30]],
#                   [r10, [150, -40]],
#                   [r11, [150, -50]],
#                   [r12, [150, -60]],
#                   [r13, [150, -70]],
#                   [r14, [150, -80]],
#                   [r15, [150, -90]],
#                   [r16, [150, -100]],
#                   [r17, [150, -110]],
#                   [r18, [150, -120]],
#                   ]
# WiringDiagram(list_elements, w, msp3)
# doc3.saveas("Монтажная схема двери.dxf", encoding='utf-8')

# doc4 = ezdxf.new()
# doc4.units = ezdxf.units.MM
# msp4 = doc4.modelspace()
# list_elements4 = [ [ct_a,[0,0]],
#                     [ct_b,[50,0]],
#                   [ct_c, [100, 0]],
#                   ]
#
# WiringDiagram(list_elements4, w, msp4)
# doc4.saveas("Монтажная схема отсека ТТ.dxf", encoding='utf-8')

# cm = CableMagazine()
# cm.add(cab101, cab102, cab103)
# cm.show(ax)

# ci = CableInstallation()
# ci.add(cab101, cab102, cab103)
# ci.show(ax)

print('Чертёжи сформированы.')
