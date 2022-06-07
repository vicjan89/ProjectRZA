'''Графические элементы с коннекторами.'''

from src.GraphicsElements import *

class GraphWithConnection(ElementGraph):
    '''Базовый класс для графических элементов с коннекторами.'''
    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.connections = {}

    def mov_to(self, base_point_key=None, x=0, y=0):
        if base_point_key == None:
            base_point_key = list(self.connections.keys())[0]
        dx = x - self.connections[base_point_key][0][0]
        dy = y - self.connections[base_point_key][0][1]
        super().mov_to(dx, dy)
        for i in self.connections.values():
            i[0][0] += dx
            i[0][1] += dy

    def rotate(self, angle):
        super().rotate(angle)
        for i in self.connections.values():
            i[0][0] = math.cos(math.radians(angle)) * i[0][0] - math.sin(math.radians(angle)) * i[0][1]
            i[0][1] = math.sin(math.radians(angle)) * i[0][0] - math.cos(math.radians(angle)) * i[0][1]
            if angle > 90:
                if i[1] == LEFT:
                    i[1] = RIGHT
                elif i[1] == RIGHT:
                    i[1] = LEFT


class Wire(ElementCircuit):
    '''Умный соединитель.'''

    def __init__(self, a, key_a, b, key_b, name='', cable=None, highlight=False):
        super().__init__(name, highlight=highlight)
        self.__a = a
        self.__key_a = key_a
        self.__b = b
        self.__key_b = key_b
        if cable != None:
            cable.add(self)

    def __str__(self):
        return 'Wire: '+ str(self.a) + '/' + str(self.__key_a) + ' - ' + str(self.b) + '/' + str(self.__key_b)

    def show(self, ax):
        if self.highlight:
            lw = 50
        else:
            lw = 0
        if type(self.__key_a) is int:
            key_a = abs(self.__key_a)
        else:
            key_a = self.__key_a
        if type(self.__key_b) is int:
            key_b = abs(self.__key_b)
        else:
            key_b = self.__key_b
        xa = self.__a.connections[key_a][1].connections[key_a][0][0]
        ya = self.__a.connections[key_a][1].connections[key_a][0][1]
        xb = self.__b.connections[key_b][1].connections[key_b][0][0]
        yb = self.__b.connections[key_b][1].connections[key_b][0][1]
        side_a = self.__a.connections[key_a][1].connections[key_a][1]
        side_b = self.__b.connections[key_b][1].connections[key_b][1]
        visible_a = self.__a.connections[key_a][1].visible
        visible_b = self.__b.connections[key_b][1].visible
        if not visible_a and not visible_b:
            self.__b.connections[key_b][1].mov_to()
            self.__b.connections[key_b][1].show(ax)
            visible_b = True
        if visible_a and visible_b:
            if xa == xb:
                if side_a == LEFT:
                    dx = -5
                elif side_a == RIGHT:
                    dx = 5
                else:
                    dx = 0
                ax.add_lwpolyline(((xa, ya), (xa + dx, ya), (xb + dx, yb), (xb, yb)), dxfattribs={'lineweight':lw})
                ax.add_text(self.name, dxfattribs={'style' : 'cyrillic_ii'}).set_pos((xa, ya + (yb - ya) / 2))
            else:
                ax.add_lwpolyline(((xa, ya), (xa, yb), (xb, yb)), dxfattribs={'lineweight':lw})
                ax.add_text(self.name, dxfattribs={'style' : 'cyrillic_ii'}).set_pos((xa, yb))
        elif visible_a and not visible_b:
            if side_a == RIGHT or side_a == BOTH:
                xm = xa + 20
                ym = ya
                ax.add_line((xa, ya), (xm, ym), dxfattribs={'lineweight':lw})
                ax.add_text(self.name, dxfattribs={'style' : 'cyrillic_ii'}).set_pos((xa + 5, ya + 5))
            elif side_a == LEFT:
                xm = xa
                ym = ya - 25
                ax.add_lwpolyline([(xa, ya), (xa - 5, ya), (xa - 5, ya - 25), (xm, ym)], dxfattribs={'lineweight':lw})
                ax.add_text(self.name, dxfattribs={'style' : 'cyrillic_ii'}).set_pos((xa, ya - 15))
            self.__b.connections[key_b][1].mov_to(base_point_key=key_b, x=xm, y=ym)
            self.__b.connections[key_b][1].show(ax)
        elif visible_b and not visible_a:
            if side_b == LEFT or side_b == BOTH:
                xm = xb - 20
                ym = yb
                ax.add_line((xb, yb), (xm, ym), dxfattribs={'lineweight':lw})
                ax.add_text(self.name, dxfattribs={'style' : 'cyrillic_ii'}).set_pos((xb - 10, yb + 5))
            elif side_b == RIGHT:
                xm = xb
                ym = yb - 25
                ax.add_lwpolyline([(xb, yb), (xb + 5, yb), (xb + 5, yb - 25), (xm, ym)], dxfattribs={'lineweight':lw})
                ax.add_text(self.name, dxfattribs={'style' : 'cyrillic_ii'}).set_pos((xb, yb - 15))
            self.__a.connections[key_a][1].mov_to(base_point_key=key_a, x=xm, y=ym)
            self.__a.connections[key_a][1].show(ax)


    def show_wd(self, ax, coords):
        if self.highlight:
            lw = 50
        else:
            lw = 0
        xa = self.__a.connections[self.__key_a][0][0]
        ya = self.__a.connections[self.__key_a][0][1]
        xb = self.__b.connections[self.__key_b][0][0]
        yb = self.__b.connections[self.__key_b][0][1]
        side_a = self.__a.connections[self.__key_a][2]
        side_b = self.__b.connections[self.__key_b][2]
        visible_a = self.__a.visible
        visible_b = self.__b.visible
        if type(self.__key_a) is int:
            key_a = abs(self.__key_a)
        else:
            key_a = self.__key_a
        if type(self.__key_b) is int:
            key_b = abs(self.__key_b)
        else:
            key_b = self.__key_b
        name_a = self.__a.name + '-' + str(key_a)
        name_b = self.__b.name + '-' + str(key_b)
        list_coords = []
        if visible_a:
            if side_a == LEFT or side_a == RIGHT:
                match coords.count((xa, ya)):
                    case 0:
                        dy = 0
                    case 1:
                        dy = -4
                    case 2:
                        dy = 4
            if side_a == DOWN or side_a == UP:
                match coords.count((xa, ya)):
                    case 0:
                        dx = 0
                    case 1:
                        dx = -4
                    case 2:
                        dx = 4
            if side_a == LEFT:
                dx = -5
                d2x = -10
                d2y = 0
                a = 'BOTTOM_RIGHT'
                f = 0
            elif side_a == RIGHT:
                dx = 5
                d2x = 10
                d2y = 0
                a = 'BOTTOM_LEFT'
                f = 0
            elif side_a == DOWN:
                dy = -5
                d2x = 0
                d2y = -10
                a = 'BOTTOM_RIGHT'
                f = 90
            elif side_a == UP:
                dy = 5
                d2x = 0
                d2y = 10
                a = 'BOTTOM_LEFT'
                f = 90
            ax.add_lwpolyline(((xa, ya), (xa + dx, ya + dy), (xa + dx + d2x, ya + dy + d2y)), dxfattribs={'lineweight':lw})
            ax.add_text(name_b, dxfattribs={'style' : 'cyrillic_ii', 'rotation':f}).set_pos((xa + dx, ya + dy), align=a)
            list_coords.append((xa, ya))
        if visible_b:
            if side_b == LEFT or side_b == RIGHT:
                match coords.count((xb, yb)):
                    case 0:
                        dy = 0
                    case 1:
                        dy = -4
                    case 2:
                        dy = 4
            if side_b == DOWN or side_b == UP:
                match coords.count((xb, yb)):
                    case 0:
                        dx = 0
                    case 1:
                        dx = -4
                    case 2:
                        dx = 4
            if side_b == LEFT:
                dx = -5
                d2x = -10
                d2y = 0
                a = 'BOTTOM_RIGHT'
                f = 0
            elif side_b == RIGHT:
                dx = 5
                d2x = 10
                d2y = 0
                a = 'BOTTOM_LEFT'
                f = 0
            elif side_b == DOWN:
                dy = -5
                d2x = 0
                d2y = -10
                a = 'BOTTOM_RIGHT'
                f = 90
            elif side_b == UP:
                dy = 5
                d2x = 0
                d2y = 10
                a = 'BOTTOM_LEFT'
                f = 90
            ax.add_lwpolyline(((xb, yb), (xb + dx, yb + dy), (xb + dx + d2x, yb + dy + d2y)), dxfattribs={'lineweight':lw})
            ax.add_text(name_a, dxfattribs={'style' : 'cyrillic_ii', 'rotation':f}).set_pos((xb + dx, yb + dy), align=a)
            list_coords.append((xb, yb))
        return list_coords

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def a_visible(self):
        return self.__a.connections[self.__key_a][1].visible

    @property
    def b_visible(self):
        return self.__b.connections[self.__key_b][1].visible

    @property
    def key_a(self):
        return self.__key_a

    @property
    def key_b(self):
        return self.__key_b


class ConnectionTerminal(GraphWithConnection):
    '''Клемма.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.centers = [[0, 0], [0, 0], [0, 0]]
        self.radii = [0.5, 0.3, 0.1]
        self.labels_xy = [[0, -5]]
        self.labels = [name]
        self.connections[name] = [[0, 0], BOTH]


class Connector(GraphWithConnection):
    '''Разъёмное соединение.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self += ConnectionDetachable()
        self.connections['s' + str(name)] = [[0, 0], LEFT]
        self.connections['p' + str(name)] = [[2, 0], RIGHT]


class Connectors(GraphWithConnection):
    '''Разъём на много соединений.'''

    def __init__(self, name='', quantity=32, highlight=False):
        super().__init__(name, highlight=highlight)
        self.n = [None]
        for i in range(1, quantity + 1):
            self.n.append(Connector(i))
            c = ConnectionDetachable(i)
            c.mov_to(0, -i * 12 - 12)
            self += c
            self.connections['s' + str(i)] = [[0, -i * 12 - 12], self.n[-1], LEFT]
            self.connections['p' + str(i)] = [[2, -i * 12 - 12], self.n[-1], RIGHT]


class CT2(GraphWithConnection):
    '''Трансформатор тока с двумя вторичными обмотками.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.w1 = GraphWithConnection(highlight=highlight)
        self.w1 += CT_W(name + '-1')
        self.w1.connections['1И1'] = [[0, 0], LEFT]
        self.w1.connections['1И2'] = [[4, 0], RIGHT]
        self.w1.labels += ['1U1', '1U2']
        self.w1.labels_xy += [[-2, -5], [6, -5]]
        self.w2 = GraphWithConnection(highlight=highlight)
        self.w2 += CT_W(name + '-2')
        self.w2.connections['2И1'] = [[0, 0], LEFT]
        self.w2.connections['2И2'] = [[4, 0], RIGHT]
        self.vertices = [[0, 0], [15, 0], [15, -55], [0, -55], [0, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels_xy = [[7, 5], [5, -5], [5, -20], [5, -35], [5, -50]]
        self.labels = [name, '1U1', '1U2', '2U1', '2U2']
        self.connections['1И1'] = [[0, -5], self.w1, LEFT]
        self.connections['1И2'] = [[0, -20], self.w1, LEFT]
        self.connections['2И1'] = [[0, -35], self.w2, LEFT]
        self.connections['2И2'] = [[0, -50], self.w2, LEFT]

class CT3(CT2):
    '''Трансформатор тока с тремя вторичными обмотками.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.w3 = GraphWithConnection(highlight=highlight)
        self.w3 += CT_W(name + '-3')
        self.w3.connections['3И1'] = [[0, 0], LEFT]
        self.w3.connections['3И2'] = [[4, 0], RIGHT]
        self.w3.labels += ['3И1', '3И2']
        self.w3.labels_xy += [[-2, -5], [6, -5]]
        self.vertices = [[0, 0], [15, 0], [15, -85], [0, -85], [0, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels_xy += [[5,-65],[5,-80]]
        self.labels += ['3И1', '3И2']
        self.connections['3И1'] = [[0, -65], self.w3, LEFT]
        self.connections['3И2'] = [[0, -80], self.w3, LEFT]


class YA(GraphWithConnection):
    '''Электромагнит управления коммутационным аппаратом.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.w = GraphWithConnection(highlight=highlight)
        self.w += Winding(name)
        self.w.connections[1] = [[0, 0], LEFT]
        self.w.connections[2] = [[15, 0], RIGHT]
        self += Winding(name)
        self.connections[1] = [[0, 0], self.w, LEFT]
        self.connections[2] = [[15, 0], self.w, RIGHT]


class RP23(GraphWithConnection):
    '''Реле промежуточное типа РП-23'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'РП-23'
        self.k1 = GraphWithConnection()
        self.k1 += ContactClose(name, highlight=highlight)
        self.k1.labels += [1, 2]
        self.k1.labels_xy += [[0, 0], [20, 0]]
        self.k1.connections[1] = [[0, 0], LEFT]
        self.k1.connections[2] = [[20, 0], RIGHT]
        self.k2 = GraphWithConnection()
        self.k2 += ContactOpen(name, highlight=highlight)
        self.k2.labels += [3, 4]
        self.k2.labels_xy += [[0, 0], [20, 0]]
        self.k2.connections[3] = [[0, 0], LEFT]
        self.k2.connections[4] = [[20, 0], RIGHT]
        self.k3 = GraphWithConnection()
        self.k3 += ContactOpen(name, highlight=highlight)
        self.k3.labels += [5, 6]
        self.k3.labels_xy += [[0, 0], [20, 0]]
        self.k3.connections[5] = [[0, 0], LEFT]
        self.k3.connections[6] = [[20, 0], RIGHT]
        self.k4 = GraphWithConnection()
        self.k4 += ContactOpen(name, highlight=highlight)
        self.k4.labels += [7, 8]
        self.k4.labels_xy += [[0, 0], [20, 0]]
        self.k4.connections[7] = [[0, 0], LEFT]
        self.k4.connections[8] = [[20, 0], RIGHT]
        self.k5 = GraphWithConnection()
        self.k5 += ContactOpen(name, highlight=highlight)
        self.k5.labels += [9, 10]
        self.k5.labels_xy += [[0, 0], [20, 0]]
        self.k5.connections[9] = [[0, 0], LEFT]
        self.k5.connections[10] = [[20, 0], RIGHT]
        self.w = GraphWithConnection()
        self.w += Winding(name, highlight=highlight)
        self.w.labels += [11, 12]
        self.w.labels_xy += [[0, 0], [15, 0]]
        self.w.connections[11] = [[0, 0], LEFT]
        self.w.connections[12] = [[15, 0], RIGHT]
        self.vertices += [[0, 0], [20, 0], [20, -75], [0, -75], [0, 0]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels += [self.type, name]
        self.labels_xy += [[10, -4], [10, 0]]
        k = ContactClose(highlight=highlight)
        k.mov_to(0, -10)
        self += k
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -20)
        self += k
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -30)
        self += k
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -40)
        self += k
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -50)
        self += k
        w = Winding(highlight=highlight)
        w.mov_to(2.5, -60)
        self += w
        self.connections[1] = [[0, -10], self.k1, LEFT]
        self.connections[2] = [[20, -10], self.k1, RIGHT]
        self.connections[3] = [[20, -20], self.k2, RIGHT]
        self.connections[4] = [[0, -20], self.k2, LEFT]
        self.connections[5] = [[20, -30], self.k3, RIGHT]
        self.connections[6] = [[20, -30], self.k3, RIGHT]
        self.connections[7] = [[0, -40], self.k4, LEFT]
        self.connections[8] = [[20, -40], self.k4, RIGHT]
        self.connections[9] = [[20, -50], self.k5, LEFT]
        self.connections[10] = [[20, -50], self.k5, RIGHT]
        self.connections[11] = [[0, -60], self.w, LEFT]
        self.connections[12] = [[20, -60], self.w, RIGHT]
        for key, value in self.connections.items():
            self.labels += [key]
            dx = 3 if value[0][0] == 0 else -3
            self.labels_xy += [[value[0][0] + dx, value[0][1]]]


class RP25(RP23):
    '''Реле промежуточное типа РП-25'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'РП-25'


class XT(GraphWithConnection):
    '''Клеммник'''

    def __init__(self, name='', quantity=50, type='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.__type = type
        self.n = [None]
        h = 6
        for i in range(1, quantity + 1):
            self.n.append(ConnectionTerminal(i, highlight=highlight))
            self.connections[i] = [[0, -i * h - 3], self.n[-1], LEFT]
            self.connections[-i] = [[20, -i * h - 3], self.n[-1], RIGHT]
            self.vertices += [[0, -i * h], [20, -i * h], [20, -i * h - h], [0, -i * h - h], [0, -i * h]]
            self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
            self.labels += [i]
            self.labels_xy += [[10, -i * h - h + 1]]
        self.labels += [name]
        self.labels_xy += [[10, 0]]


class RP361(GraphWithConnection):
    '''Реле РП-361'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.k2_4_6 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name)
        k.rotate(180)
        k.mov_to(20, 0)
        self.k2_4_6 += k
        k = ContactClose(name)
        k.rotate(180)
        k.mov_to(20, 20)
        self.k2_4_6 += k
        self.k2_4_6.vertices += [[20, 0], [20, 20]]
        self.k2_4_6.codes += [Path.MOVETO, Path.LINETO]
        self.k2_4_6.connections[2] = [[0, 0], LEFT]
        self.k2_4_6.connections[4] = [[20, 0], RIGHT]
        self.k2_4_6.connections[6] = [[0, 20], LEFT]
        self.k2_4_6.labels += [2, 4, 6]
        self.k2_4_6.labels_xy += [[0, -4], [20, -4], [0, 16]]
        self.w8_14 = GraphWithConnection(highlight=highlight)
        self.w8_14 += Winding(name)
        self.w8_14.connections[8] = [[0, 0], LEFT]
        self.w8_14.connections[14] = [[15, 0], RIGHT]
        self.w8_14.labels += [8, 14]
        self.w8_14.labels_xy += [[0, -4], [15, -4]]
        self.vertices = [[0, 0], [20, 0], [20, -70], [0, -70], [0, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels = [name, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 'РП-361']
        self.labels_xy = [[10, 0], [17, -7], [3, -7], [17, -17], [3, -17], [17, -27], [3, -27], [17, -37], [3, -37],
                          [17, -47], [3, -47],
                          [17, -57], [3, -57], [17, -67], [3, -67], [10, -5]]
        self.connections[1] = [[20, -5], self.k2_4_6, RIGHT]
        self.connections[2] = [[0, -5], self.k2_4_6, LEFT]
        self.connections[3] = [[20, -15], self.k2_4_6, RIGHT]
        self.connections[4] = [[0, -15], self.k2_4_6, LEFT]
        self.connections[5] = [[20, -25], self.k2_4_6, RIGHT]
        self.connections[6] = [[0, -25], self.k2_4_6, LEFT]
        self.connections[7] = [[30, -35], self.k2_4_6, RIGHT]
        self.connections[8] = [[0, -35], self.w8_14, LEFT]
        self.connections[9] = [[30, -45], self.k2_4_6, RIGHT]
        self.connections[10] = [[0, -45], self.k2_4_6, LEFT]
        self.connections[11] = [[30, -55], self.k2_4_6, RIGHT]
        self.connections[12] = [[0, -55], self.k2_4_6, LEFT]
        self.connections[13] = [[30, -65], self.k2_4_6, RIGHT]
        self.connections[14] = [[0, -65], self.w8_14, LEFT]


class BPT615(GraphWithConnection):
    '''Блок питания БПТ-615 производства ОАО "БЭМН" г.Минск.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.k1_2 = GraphWithConnection(highlight=highlight)
        self.k1_2 += Winding(name)
        self.k1_2.connections[2] = [[0, 0], LEFT]
        self.k1_2.connections[1] = [[15, 0], RIGHT]
        self.k1_2.labels += [2, 1]
        self.k1_2.labels_xy += [[0, -4], [15, -4]]
        self.k3_4 = GraphWithConnection(highlight=highlight)
        self.k3_4 += Winding(name)
        self.k3_4.connections[4] = [[0, 0], LEFT]
        self.k3_4.connections[3] = [[15, 0], RIGHT]
        self.k3_4.labels += [4, 3]
        self.k3_4.labels_xy += [[0, -4], [15, -4]]
        self.vertices = [[0, 0], [20, 0], [20, -120], [0, -120], [0, 0]]
        self.codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels = [name, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 'БПТ-615']
        self.labels_xy = [[10, 0], [17, -65], [17, -55], [17, -45], [17, -35], [3, -115], [3, -105], [3, -95], [3, -85],
                          [3, -75], [3, -65], [3, -55], [3, -45], [3, -35], [3, -25], [3, -15], [3, -5], [15, -5]]
        self.connections[1] = [[20, -65], self.k1_2, RIGHT]
        self.connections[2] = [[20, -55], self.k1_2, RIGHT]
        self.connections[3] = [[20, -45], self.k3_4, RIGHT]
        self.connections[4] = [[20, -35], self.k3_4, RIGHT]
        self.connections[5] = [[0, -115], self.k1_2, LEFT]
        self.connections[6] = [[0, -105], self.k1_2, LEFT]
        self.connections[7] = [[0, -95], self.k3_4, LEFT]
        self.connections[8] = [[0, -85], self.k3_4, LEFT]
        self.connections[9] = [[0, -75], self.k1_2, LEFT]
        self.connections[10] = [[0, -65], self.k1_2, LEFT]
        self.connections[11] = [[0, -55], self.k3_4, LEFT]
        self.connections[12] = [[0, -45], self.k3_4, LEFT]
        self.connections[13] = [[0, -35], self.k1_2, LEFT]
        self.connections[14] = [[0, -25], self.k1_2, LEFT]
        self.connections[15] = [[0, -15], self.k3_4, LEFT]
        self.connections[16] = [[0, -5], self.k3_4, LEFT]


class MR5PO50(GraphWithConnection):
    '''Класс для описания микропроцессорного реле МР5ПО50 производства ОАО "БЭМН" г.Минск.'''

    def __init__(self, name='', highlight=False):
        '''Конструктор класса МР5ПО50.'''
        super().__init__(name, highlight)
        self.x8 = GraphWithConnection(highlight=highlight)
        self.x8.vertices += [[0, 0], [25, 0], [25, -150], [0, -150], [0, 0]]
        self.x8.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.x8.connections['X8:1'] = [[0, -12], LEFT]
        self.x8.connections['X8:2'] = [[25, -12], RIGHT]
        self.x8.connections['X8:4'] = [[0, -37], LEFT]
        self.x8.connections['X8:5'] = [[25, -37], RIGHT]
        self.x8.connections['X8:7'] = [[0, -62], LEFT]
        self.x8.connections['X8:8'] = [[25, -62], RIGHT]
        self.x8.connections['X8:10'] = [[0, -112], LEFT]
        self.x8.connections['X8:11'] = [[0, -137], LEFT]
        self.x8.connections['X8:12'] = [[25, -112], RIGHT]
        self.x8.labels += [name, 'X8:1', 'X8:2', 'X8:4', 'X8:5', 'X8:7', 'X8:8', 'X8:10', 'X8:11', 'X8:12', 'Ia', 'Ib',
                           'Ic', 'In']
        self.x8.labels_xy += [[12, 5], [5, -14], [20, -14], [5, -39], [20, -39], [5, -64], [20, -64], [5, -114],
                              [20, -139], [20, -114],
                              [12, -10], [12, -35], [12, -60], [12, -110]]
        self.x2_1_2 = GraphWithConnection(highlight=highlight)
        self.x2_1_2 += ContactClose('Рн')
        self.x2_1_2.labels += ['X2:1', 'X2:2']
        self.x2_1_2.labels_xy += [[0, -4], [20, -4]]
        self.x2_1_2.connections['X2:1'] = [[0, 0], LEFT]
        self.x2_1_2.connections['X2:2'] = [[20, 0], RIGHT]
        self.x2_3_4 = GraphWithConnection(highlight=highlight)
        self.x2_3_4 += ContactOpen('Рвкл')
        self.x2_3_4.labels += ['X2:3', 'X2:4']
        self.x2_3_4.labels_xy += [[0, -4], [20, -4]]
        self.x2_3_4.connections['X2:3'] = [[0, 0], LEFT]
        self.x2_3_4.connections['X2:4'] = [[20, 0], RIGHT]
        self.x2_5_6 = GraphWithConnection(highlight=highlight)
        self.x2_5_6 += ContactOpen('Роткл1')
        self.x2_5_6.labels += ['X2:5', 'X2:6']
        self.x2_5_6.labels_xy += [[0, -4], [20, -4]]
        self.x2_5_6.connections['X2:5'] = [[0, 0], LEFT]
        self.x2_5_6.connections['X2:6'] = [[20, 0], RIGHT]
        self.x2_7_8 = GraphWithConnection(highlight=highlight)
        self.x2_7_8 += ContactOpen('Роткл2')
        self.x2_7_8.labels += ['X2:7', 'X2:8']
        self.x2_7_8.labels_xy += [[0, -4], [20, -4]]
        self.x2_7_8.connections['X2:7'] = [[0, 0], LEFT]
        self.x2_7_8.connections['X2:8'] = [[20, 0], RIGHT]
        self.x1_1_2 = GraphWithConnection(highlight=highlight)
        self.x1_1_2 += Power(name)
        self.x1_1_2.labels += ['Uп', 'X1:1', 'X1:2']
        self.x1_1_2.labels_xy += [[10, 0], [0, -4], [20, -4]]
        self.x1_1_2.connections['X1:1'] = [[0, 0], LEFT]
        self.x1_1_2.connections['X1:2'] = [[20, 0], RIGHT]
        self.x4 = []
        self.x5 = []
        self.x6 = []
        for i in range(8):
            self.x4.append(GraphWithConnection(highlight=highlight))
            self.x4[i] += ContactOpen(name + 'Р' + str(i + 1))
            self.x4[i].labels += ['X4:' + str(i * 2 + 1), 'X4:' + str(i * 2 + 2)]
            self.x4[i].labels_xy += [[0, -2],[20,-2]]
            self.x4[i].connections['X4:' + str(i * 2 + 1)] = [[0,0],LEFT]
            self.x4[i].connections['X4:' + str(i * 2 + 2)] = [[20, 0], RIGHT]
            self.connections['X4:' + str(i * 2 + 1)] = [[0, -225 - i * 20], self.x4[i], LEFT]
            self.connections['X4:' + str(i * 2 + 2)] = [[0, -235 - i * 20], self.x4[i], LEFT]
            self.x5.append(GraphWithConnection(highlight=highlight))
            self.x5[i] += Power(name + 'Д' + str(i + 1),highlight=highlight)
            self.x5[i].labels += ['X5:' + str(i * 2 + 1), 'X5:' + str(i * 2 + 2)]
            self.x5[i].labels_xy += [[0, -2],[20,-2]]
            self.x5[i].connections['X5:' + str(i * 2 + 1)] = [[0,0],LEFT]
            self.x5[i].connections['X5:' + str(i * 2 + 2)] = [[20, 0], RIGHT]
            self.connections['X5:' + str(i * 2 + 1)] = [[25, -225 - i * 20], self.x5[i], RIGHT]
            self.connections['X5:' + str(i * 2 + 2)] = [[25, -235 - i * 20], self.x5[i], RIGHT]
            self.x6.append(GraphWithConnection(highlight=highlight))
            self.x6[i] += Power(name + 'Д' + str(i + 9),highlight=highlight)
            self.x6[i].labels += ['X6:' + str(i * 2 + 9), 'X6:' + str(i * 2 + 10)]
            self.x6[i].labels_xy += [[0, -2],[20,-2]]
            self.x6[i].connections['X6:' + str(i * 2 + 9)] = [[0,0],LEFT]
            self.x6[i].connections['X6:' + str(i * 2 + 10)] = [[20, 0], RIGHT]
            self.connections['X6:' + str(i * 2 + 9)] = [[25, -5 - i * 20], self.x6[i], RIGHT]
            self.connections['X6:' + str(i * 2 + 10)] = [[25, -15 - i * 20], self.x6[i], RIGHT]
        self.connections['X1:1'] = [[0, -195], self.x1_1_2, LEFT]
        self.connections['X1:2'] = [[0, -205], self.x1_1_2, LEFT]
        self.connections['X2:1'] = [[0, -105], self.x2_1_2, LEFT]
        self.connections['X2:2'] = [[0, -115], self.x2_1_2, LEFT]
        self.connections['X2:3'] = [[0, -125], self.x2_3_4, LEFT]
        self.connections['X2:4'] = [[0, -135], self.x2_3_4, LEFT]
        self.connections['X2:5'] = [[0, -145], self.x2_5_6, LEFT]
        self.connections['X2:6'] = [[0, -155], self.x2_5_6, LEFT]
        self.connections['X2:7'] = [[0, -165], self.x2_7_8, LEFT]
        self.connections['X2:8'] = [[0, -175], self.x2_7_8, LEFT]
        self.connections['X8:1'] = [[0, -5], self.x8, LEFT]
        self.connections['X8:2'] = [[0, -15], self.x8, LEFT]
        self.connections['X8:4'] = [[0, -25], self.x8, LEFT]
        self.connections['X8:5'] = [[0, -35], self.x8, LEFT]
        self.connections['X8:7'] = [[0, -45], self.x8, LEFT]
        self.connections['X8:8'] = [[0, -55], self.x8, LEFT]
        self.connections['X8:10'] = [[0, -65], self.x8, LEFT]
        self.connections['X8:11'] = [[0, -75], self.x8, LEFT]
        self.connections['X8:12'] = [[0, -85], self.x8, LEFT]
        self.vertices += [[0,5],[25,5],[25,-380],[0,-380],[0,5]]
        self.codes += [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO]
        self.labels += [name, 'МР5ПО50']
        self.labels_xy += [[12,5], [12,0]]
        for key, value in self.connections.items():
            self.labels += [key]
            dx = 4 if value[0][0] == 0 else -4
            self.labels_xy += [[value[0][0]+dx,value[0][1]]]


class BB_TEL10(GraphWithConnection):
    '''Вакуумный выключатель BB/TEL-10'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.sf1 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name+'-SF1')
        self.sf1 += k
        self.sf1.connections[1] = [[0, 0], LEFT]
        self.sf1.connections[2] = [[20, 0], RIGHT]
        self.sf2 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name + '-SF2')
        self.sf2 += k
        self.sf2.connections[3] = [[0, 0], LEFT]
        self.sf2.connections[4] = [[20, 0], RIGHT]
        self.sf3 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name + '-SF3')
        self.sf3 += k
        self.sf3.connections[5] = [[0, 0], LEFT]
        self.sf3.connections[6] = [[20, 0], RIGHT]
        self.sf4 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name + '-SF4')
        self.sf4 += k
        self.sf4.connections[7] = [[0, 0], LEFT]
        self.sf4.connections[8] = [[20, 0], RIGHT]
        self.sf5 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name + '-SF5')
        self.sf5 += k
        self.sf5.connections[9] = [[0, 0], LEFT]
        self.sf5.connections[10] = [[20, 0], RIGHT]
        self.sf6 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name + '-SF6')
        self.sf6 += k
        self.sf6.connections[11] = [[0, 0], LEFT]
        self.sf6.connections[12] = [[20, 0], RIGHT]
        self.em = GraphWithConnection(highlight=highlight)
        k = Winding(name + '-ЭМ1')
        self.em += k
        self.em.connections[13] = [[0, 0], LEFT]
        self.em.connections[14] = [[20, 0], RIGHT]
        self.bk = GraphWithConnection(highlight=highlight)
        k = ContactClose(name + '-БК')
        self.bk += k
        self.bk.connections[15] = [[0, 0], LEFT]
        self.bk.connections[16] = [[20, 0], RIGHT]
        self.sf7 = GraphWithConnection(highlight=highlight)
        k = ContactClose(name + '-SF7')
        self.sf7 += k
        self.sf7.connections[17] = [[0, 0], LEFT]
        self.sf7.connections[18] = [[20, 0], RIGHT]
        self.sf8 = GraphWithConnection(highlight=highlight)
        k = ContactClose(name + '-SF8')
        self.sf8 += k
        self.sf8.connections[19] = [[0, 0], LEFT]
        self.sf8.connections[20] = [[20, 0], RIGHT]
        self.sf9 = GraphWithConnection(highlight=highlight)
        k = ContactClose(name + '-SF9')
        self.sf9 += k
        self.sf9.connections[21] = [[0, 0], LEFT]
        self.sf9.connections[22] = [[20, 0], RIGHT]
        self.sf10 = GraphWithConnection(highlight=highlight)
        k = ContactClose(name + '-SF10')
        self.sf10 += k
        self.sf10.connections[23] = [[0, 0], LEFT]
        self.sf10.connections[24] = [[20, 0], RIGHT]
        self.sf11 = GraphWithConnection(highlight=highlight)
        k = ContactClose(name + '-SF11')
        self.sf11 += k
        self.sf11.connections[25] = [[0, 0], LEFT]
        self.sf11.connections[26] = [[20, 0], RIGHT]
        self.sf12 = GraphWithConnection(highlight=highlight)
        k = ContactClose(name + '-SF12')
        self.sf12 += k
        self.sf12.connections[27] = [[0, 0], LEFT]
        self.sf12.connections[28] = [[20, 0], RIGHT]
        self.connections[1] = [[0, -10], self.sf1, LEFT]
        self.connections[2] = [[0, -20], self.sf1, LEFT]
        self.connections[3] = [[0, -30], self.sf2, LEFT]
        self.connections[4] = [[0, -40], self.sf2, LEFT]
        self.connections[5] = [[0, -50], self.sf3, LEFT]
        self.connections[6] = [[0, -60], self.sf3, LEFT]
        self.connections[7] = [[0, -70], self.sf4, LEFT]
        self.connections[8] = [[0, -80], self.sf4, LEFT]
        self.connections[9] = [[0, -90], self.sf5, LEFT]
        self.connections[10] = [[0, -100], self.sf5, LEFT]
        self.connections[11] = [[0, -110], self.sf6, LEFT]
        self.connections[12] = [[0, -120], self.sf6, LEFT]
        self.connections[13] = [[0, -130], self.em, LEFT]
        self.connections[14] = [[0, -140], self.em, LEFT]
        self.connections[15] = [[20, -10], self.bk, RIGHT]
        self.connections[16] = [[20, -20], self.bk, RIGHT]
        self.connections[17] = [[20, -30], self.sf7, RIGHT]
        self.connections[18] = [[20, -40], self.sf7, RIGHT]
        self.connections[19] = [[20, -50], self.sf8, RIGHT]
        self.connections[20] = [[20, -60], self.sf8, RIGHT]
        self.connections[21] = [[20, -70], self.sf9, RIGHT]
        self.connections[22] = [[20, -80], self.sf9, RIGHT]
        self.connections[23] = [[20, -90], self.sf10, RIGHT]
        self.connections[24] = [[20, -100], self.sf10, RIGHT]
        self.connections[25] = [[20, -110], self.sf11, RIGHT]
        self.connections[26] = [[20, -120], self.sf11, RIGHT]
        self.connections[27] = [[20, -130], self.sf12, RIGHT]
        self.connections[28] = [[20, -140], self.sf12, RIGHT]
        self.vertices += [[0, 0], [20, 0], [20, -145], [0, -145], [0, 0]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels += [name, 'BB/TEL-10']
        self.labels_xy += [[10, 0], [10, -5],]
        for key, value in self.connections.items():
            self.labels += [key]
            dx = 4 if value[0][0] == 0 else -4
            self.labels_xy += [[value[0][0]+dx,value[0][1]]]


class PS7(GraphWithConnection):
    '''Панель сигнальная ПС7 Сиинтез-Электро.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'ПС-7'
        self.vertices += [[5,0],[185,0],[185,-20],[5,-20],[5,0]]
        self.codes += [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO]
        self.l_bi = []
        for i in range(7):
            self.l_bi.append(GraphWithConnection(name, highlight=highlight))
            self.l_bi[-1] += BI('Вход ' + str(i+1), highlight=highlight)
            self.l_bi[-1].labels += [name, i * 2 + 5, i * 2 + 6]
            self.l_bi[-1].labels_xy += [[10,2],[0, -2],[20,-2]]
            self.l_bi[-1].connections[i * 2 + 5] = [[0,0],LEFT]
            self.l_bi[-1].connections[i * 2 + 6] = [[20, 0], RIGHT]
            self.connections[i * 2 + 5] = [[i*20 + 50,-20], self.l_bi[-1], DOWN]
            self.connections[i * 2 + 6] = [[i*20 + 60,-20], self.l_bi[-1], DOWN]
            self.labels += ['Вход ' + str(i+1), i * 2 + 5, i * 2 + 6]
            self.labels_xy += [[i*20 + 55,-12],[i*20 + 50,-18],[i*20 + 60,-18]]
        self.p = GraphWithConnection(highlight=highlight)
        self.p += Power('Сеть',highlight=highlight)
        self.p.labels += [name, 1, 2]
        self.p.labels_xy += [[10,6], [0,0],[20,0]]
        self.p.connections[1] = [[0,0],LEFT]
        self.p.connections[2] = [[20, 0], RIGHT]
        self.connections[1] = [[10,-20],self.p,DOWN]
        self.connections[2] = [[20, -20], self.p, DOWN]
        self.labels += ['Сеть',1,2]
        self.labels_xy += [[15,-12],[10,-18],[20,-18]]
        self.r = GraphWithConnection()
        self.r += ContactOpen('Реле', highlight=highlight)
        self.r.labels += [name, 3, 4]
        self.r.labels_xy += [[5, 6], [0, 0], [20, 0]]
        self.r.connections[3] = [[0, 0], LEFT]
        self.r.connections[4] = [[20, 0], RIGHT]
        self.connections[3] = [[30, -20], self.r, DOWN]
        self.connections[4] = [[40, -20], self.r, DOWN]
        self.labels += [self.type,name,'Реле',3, 4]
        self.labels_xy += [[95,-5],[95,0],[35,-12],[30, -18], [40, -18]]


class BU_TEL(GraphWithConnection):
    '''Блок управления BU/TEL-220-05A выключателем BB/TEL-10'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Блок управления BU/TEL-220-05A выключателем BB/TEL-10'
        self.xt1_9 = GraphWithConnection(highlight=highlight)
        self.xt1_9.vertices += [[0,0], [20,0],[20,-100],[0,-100],[0,0]]
        self.xt1_9.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.xt1_9.labels += [name,'1 +220','2 -220', '3 ЭМ1','4 ЭМ2','5 БК1','6 БК2','7 ВО',
                              '8 ВКЛ','9 ОТКЛ']
        self.xt1_9.labels_xy += [[10,0],[3,-10],[3,-20],[3,-30],[3,-40],[3,-50],[3,-60],[3,-70],[3,-80],[3,-90]]
        self.xt1_9.connections[1] = [[0,-10],LEFT]
        self.xt1_9.connections[2] = [[0, -20], LEFT]
        self.xt1_9.connections[3] = [[0, -30], LEFT]
        self.xt1_9.connections[4] = [[0, -40], LEFT]
        self.xt1_9.connections[5] = [[0, -50], LEFT]
        self.xt1_9.connections[6] = [[0, -60], LEFT]
        self.xt1_9.connections[7] = [[0, -70], LEFT]
        self.xt1_9.connections[8] = [[0, -80], LEFT]
        self.xt1_9.connections[9] = [[0, -90], LEFT]
        self.tta = GraphWithConnection(highlight=highlight)
        self.tta += BI('TTA')
        self.tta.labels += [name, 10,11]
        self.tta.labels_xy += [[10,6],[0,0],[20,0]]
        self.tta.connections[10] = [[0,0],LEFT]
        self.tta.connections[11] = [[20, 0], RIGHT]
        self.ttc = GraphWithConnection(highlight=highlight)
        self.ttc += BI('TTC')
        self.ttc.labels += [name, 12, 13]
        self.tta.labels_xy += [[10, 6], [0, 0], [20, 0]]
        self.tta.connections[12] = [[0, 0], LEFT]
        self.tta.connections[13] = [[20, 0], RIGHT]
        self.connections[1] = [[0,-10],self.xt1_9,LEFT]
        self.connections[2] = [[0, -20], self.xt1_9, LEFT]
        self.connections[3] = [[0, -30], self.xt1_9, LEFT]
        self.connections[4] = [[0, -40], self.xt1_9, LEFT]
        self.connections[5] = [[0, -50], self.xt1_9, LEFT]
        self.connections[6] = [[0, -60], self.xt1_9, LEFT]
        self.connections[7] = [[0, -70], self.xt1_9, LEFT]
        self.connections[8] = [[0, -80], self.xt1_9, LEFT]
        self.connections[9] = [[0, -90], self.xt1_9, LEFT]
        self.connections[10] = [[0, -100], self.tta, LEFT]
        self.connections[11] = [[0, -110], self.tta, LEFT]
        self.connections[12] = [[0, -120], self.ttc, LEFT]
        self.connections[13] = [[0, -130], self.ttc, LEFT]
        self.vertices += [[0,0],[35,0],[35,-135],[0,-135],[0,0]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels += [name, 'BU/TEL-220-05A',' 1 +220', ' 2 -220', ' 3 ЭМ1 ', ' 4 ЭМ2 ', ' 5 БК1 ', ' 6 БК2 ',
                        ' 7 ВО   ', ' 8 ВКЛ ', ' 9 ОТКЛ', '10 TTA1','11 TTA2','12 TTC1','13 TTC2']
        self.labels_xy += [[17, 0], [17,-5],[1, -10, 'BOTTOM_LEFT'], [1, -20, 'BOTTOM_LEFT'], [1, -30, 'BOTTOM_LEFT'],
                           [1, -40, 'BOTTOM_LEFT'], [1, -50, 'BOTTOM_LEFT'], [1, -60, 'BOTTOM_LEFT'], [1, -70, 'BOTTOM_LEFT'],
                [1, -80, 'BOTTOM_LEFT'], [1, -90, 'BOTTOM_LEFT'],[1,-100, 'BOTTOM_LEFT'],[1,-110, 'BOTTOM_LEFT'],[1,-120, 'BOTTOM_LEFT'],[1,-130, 'BOTTOM_LEFT']]


class BP_TEL(GraphWithConnection):
    '''Блок питания BP/TEL-220-02A выключателя BB/TEL-10'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Блок питания BP/TEL-220-02A выключателя BB/TEL-10'
        self.bp = GraphWithConnection(highlight=highlight)
        self.bp.vertices += [[0, 0], [20, 0], [20, -65], [0, -65], [0, 0]]
        self.bp.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.bp.labels += [name, '14 ~220', '15 ~220', '8 +220', '9 +220', '5 -220', '6 220']
        self.bp.labels_xy += [[10, 0], [3, -10,'BOTTOM_LEFT'], [3, -20,'BOTTOM_LEFT'], [3, -30,'BOTTOM_RIGHT'],
                                 [3, -40,'BOTTOM_RIGHT'], [3, -50,'BOTTOM_RIGHT'], [3, -60,'BOTTOM_RIGHT']]
        self.bp.connections[14] = [[0, -10], LEFT]
        self.bp.connections[15] = [[0, -20], LEFT]
        self.bp.connections[8] = [[20, -30], RIGHT]
        self.bp.connections[9] = [[20, -40], RIGHT]
        self.bp.connections[5] = [[20, -50], RIGHT]
        self.bp.connections[6] = [[20, -60], RIGHT]
        self.bp12 = GraphWithConnection(highlight=highlight)
        self.bp12.vertices += [[0, 0], [20, 0], [20, -25], [0, -25], [0, 0]]
        self.bp12.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.bp12.labels += [name, '-12В 11', '+12В 12']
        self.bp12.labels_xy += [[10, 0], [20, -10,'BOTTOM_RIGHT'], [20, -20,'BOTTOM_RIGHT']]
        self.bp12.connections[11] = [[20, -10], RIGHT]
        self.bp12.connections[12] = [[20, -20], RIGHT]
        self.k = GraphWithConnection()
        self.k += ContactOpenClose(name, highlight=highlight)
        self.k.labels += [18, 17, 16]
        self.k.labels_xy += [[0, 0], [20, 7], [20, 0]]
        self.k.connections[18] = [[0, 0], LEFT]
        self.k.connections[17] = [[20, 10], RIGHT]
        self.k.connections[16] = [[20, 0], RIGHT]
        self.connections[5] = [[0, -10], self.bp, LEFT]
        self.connections[6] = [[0, -20], self.bp, LEFT]
        self.connections[8] = [[0, -30], self.bp, LEFT]
        self.connections[9] = [[0, -40], self.bp, LEFT]
        self.connections[11] = [[0, -50], self.bp12, LEFT]
        self.connections[12] = [[0, -60], self.bp12, LEFT]
        self.connections[14] = [[0, -70], self.bp, LEFT]
        self.connections[15] = [[0, -80], self.bp, LEFT]
        self.connections[16] = [[0, -90], self.k, LEFT]
        self.connections[17] = [[0, -100], self.k, LEFT]
        self.connections[18] = [[0, -110], self.k, LEFT]
        self.vertices += [[0, 0], [35, 0], [35, -115], [0, -115], [0, 0]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels += [name, 'BP/TEL-220-02A', ' 5 -220', ' 6 -220', ' 8 +220', ' 9 +220', '11 -12В', '12 +12В',
                        '14 ~220В', '15 ~220В', '16 Конт.Uвых 3', '17 Конт.Uвых 1', '18 Конт.Uвых 2']
        self.labels_xy += [[17, 0], [17, -5], [1, -10, 'BOTTOM_LEFT'], [1, -20, 'BOTTOM_LEFT'], [1, -30, 'BOTTOM_LEFT'],
                           [1, -40, 'BOTTOM_LEFT'], [1, -50, 'BOTTOM_LEFT'], [1, -60, 'BOTTOM_LEFT'], [1, -70, 'BOTTOM_LEFT'],
                           [1, -80, 'BOTTOM_LEFT'], [1, -90, 'BOTTOM_LEFT'], [1, -100, 'BOTTOM_LEFT'], [1, -110, 'BOTTOM_LEFT']]


class MR500_V2(GraphWithConnection):
    '''Класс для описания микропроцессорного реле МР500 версии до 3.0 производства ОАО "БЭМН" г.Минск.'''

    def __init__(self, name='', highlight=False):
        '''Конструктор класса МР5О0 версии до 3.0.'''
        super().__init__(name, highlight)
        self.x6 = GraphWithConnection(highlight=highlight)
        self.x6.vertices += [[0, 0], [25, 0], [25, -70], [0, -70], [0, 0]]
        self.x6.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.x6.connections['X6:1'] = [[0, -12], LEFT]
        self.x6.connections['X6:2'] = [[25, -12], RIGHT]
        self.x6.connections['X6:4'] = [[0, -37], LEFT]
        self.x6.connections['X6:5'] = [[25, -37], RIGHT]
        self.x6.connections['X6:7'] = [[0, -62], LEFT]
        self.x6.connections['X6:8'] = [[25, -62], RIGHT]
        self.x6.labels += [name, 'X6:1', 'X6:2', 'X6:4', 'X6:5', 'X6:7', 'X6:8', 'Ia', 'Ib', 'Ic']
        self.x6.labels_xy += [[12, 5], [5, -14], [20, -14], [5, -39], [20, -39], [5, -64], [20, -64], [5, -114],
                              [20, -139], [20, -114]]
        self.x2_1_2 = GraphWithConnection(highlight=highlight)
        self.x2_1_2 += ContactClose('Рн')
        self.x2_1_2.labels += ['X2:1', 'X2:2']
        self.x2_1_2.labels_xy += [[0, -4], [20, -4]]
        self.x2_1_2.connections['X2:1'] = [[0, 0], LEFT]
        self.x2_1_2.connections['X2:2'] = [[20, 0], RIGHT]
        self.x2_3_4 = GraphWithConnection(highlight=highlight)
        self.x2_3_4 += ContactOpen('Рвкл')
        self.x2_3_4.labels += ['X2:3', 'X2:4']
        self.x2_3_4.labels_xy += [[0, -4], [20, -4]]
        self.x2_3_4.connections['X2:3'] = [[0, 0], LEFT]
        self.x2_3_4.connections['X2:4'] = [[20, 0], RIGHT]
        self.x2_5_6 = GraphWithConnection(highlight=highlight)
        self.x2_5_6 += ContactOpen('Роткл1')
        self.x2_5_6.labels += ['X2:5', 'X2:6']
        self.x2_5_6.labels_xy += [[0, -4], [20, -4]]
        self.x2_5_6.connections['X2:5'] = [[0, 0], LEFT]
        self.x2_5_6.connections['X2:6'] = [[20, 0], RIGHT]
        self.x1 = GraphWithConnection(highlight=highlight)
        self.x1 += Power(name,highlight=highlight)
        self.x1.labels += ['Uп', 'X1:2', 'X1:3']
        self.x1.labels_xy += [[10, 0], [0, -4], [20, -4]]
        self.x1.connections['X1:2'] = [[0, 0], LEFT]
        self.x1.connections['X1:3'] = [[20, 0], RIGHT]
        self.x7 = []
        self.x8 = []
        self.x9 = []
        for i in range(8):
            self.x7.append(GraphWithConnection(highlight=highlight))
            self.x7[i] += ContactOpen(name + 'Р' + str(i + 1))
            self.x7[i].labels += ['X7:' + str(i * 2 + 1), 'X7:' + str(i * 2 + 2)]
            self.x7[i].labels_xy += [[0, -2],[20,-2]]
            self.x7[i].connections['X7:' + str(i * 2 + 1)] = [[0,0],LEFT]
            self.x7[i].connections['X7:' + str(i * 2 + 2)] = [[20, 0], RIGHT]
            self.connections['X7:' + str(i * 2 + 1)] = [[0, -225 - i * 20], self.x7[i], LEFT]
            self.connections['X7:' + str(i * 2 + 2)] = [[0, -235 - i * 20], self.x7[i], LEFT]
            self.x8.append(GraphWithConnection(highlight=highlight))
            self.x8[i] += Power(name + 'Д' + str(i + 1),highlight=highlight)
            self.x8[i].labels += ['X8:' + str(i * 2 + 1), 'X8:' + str(i * 2 + 2)]
            self.x8[i].labels_xy += [[0, -2],[20,-2]]
            self.x8[i].connections['X8:' + str(i * 2 + 1)] = [[0,0],LEFT]
            self.x8[i].connections['X8:' + str(i * 2 + 2)] = [[20, 0], RIGHT]
            self.connections['X8:' + str(i * 2 + 1)] = [[25, -225 - i * 20], self.x8[i], RIGHT]
            self.connections['X8:' + str(i * 2 + 2)] = [[25, -235 - i * 20], self.x8[i], RIGHT]
            self.x9.append(GraphWithConnection(highlight=highlight))
            self.x9[i] += Power(name + 'Д' + str(i + 9),highlight=highlight)
            self.x9[i].labels += ['X9:' + str(i * 2 + 9), 'X9:' + str(i * 2 + 10)]
            self.x9[i].labels_xy += [[0, -2],[20,-2]]
            self.x9[i].connections['X9:' + str(i * 2 + 1)] = [[0,0],LEFT]
            self.x9[i].connections['X9:' + str(i * 2 + 2)] = [[20, 0], RIGHT]
            self.connections['X9:' + str(i * 2 + 1)] = [[25, -5 - i * 20], self.x9[i], RIGHT]
            self.connections['X9:' + str(i * 2 + 2)] = [[25, -15 - i * 20], self.x9[i], RIGHT]
        self.connections['X1:2'] = [[0, -195], self.x1, LEFT]
        self.connections['X1:3'] = [[0, -205], self.x1, LEFT]
        self.connections['X2:1'] = [[0, -105], self.x2_1_2, LEFT]
        self.connections['X2:2'] = [[0, -115], self.x2_1_2, LEFT]
        self.connections['X2:3'] = [[0, -125], self.x2_3_4, LEFT]
        self.connections['X2:4'] = [[0, -135], self.x2_3_4, LEFT]
        self.connections['X2:5'] = [[0, -145], self.x2_5_6, LEFT]
        self.connections['X2:6'] = [[0, -155], self.x2_5_6, LEFT]
        self.connections['X6:1'] = [[0, -5], self.x6, LEFT]
        self.connections['X6:2'] = [[0, -15], self.x6, LEFT]
        self.connections['X6:4'] = [[0, -25], self.x6, LEFT]
        self.connections['X6:5'] = [[0, -35], self.x6, LEFT]
        self.connections['X6:7'] = [[0, -45], self.x6, LEFT]
        self.connections['X6:8'] = [[0, -55], self.x6, LEFT]
        self.vertices += [[0,5],[25,5],[25,-380],[0,-380],[0,5]]
        self.codes += [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO]
        self.labels += [name, 'МР500_V2']
        self.labels_xy += [[12,5], [12,0]]
        for key, value in self.connections.items():
            self.labels += [key]
            dx = 4 if value[0][0] == 0 else -4
            self.labels_xy += [[value[0][0]+dx,value[0][1]]]


class PS3_old(GraphWithConnection):
    '''Индикатор фаз ПС-3 Синтез-Электро'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Индикатор фаз ПС-3 Синтез-Электро'
        self.k1 = GraphWithConnection()
        self.k1 += ContactOpenClose('K1',highlight=highlight)
        self.k1.labels += [8,7,9]
        self.k1.labels_xy += [[0,0],[20,7],[20,0]]
        self.k1.connections[8] = [[0,0],LEFT]
        self.k1.connections[7] = [[20, 10], RIGHT]
        self.k1.connections[9] = [[20, 0], RIGHT]
        self.k1_1 = GraphWithConnection()
        self.k1_1 += ContactOpenClose('K1',highlight=highlight)
        self.k1_1.labels += [11,12,10]
        self.k1_1.labels_xy += [[0,0],[20,7],[20,0]]
        self.k1_1.connections[11] = [[0,0],LEFT]
        self.k1_1.connections[12] = [[20, 10], RIGHT]
        self.k1_1.connections[10] = [[20, 0], RIGHT]
        self.k2 = GraphWithConnection()
        self.k2 += ContactOpenClose('K2',highlight=highlight)
        self.k2.labels += [14,13,15]
        self.k2.labels_xy += [[0,0],[20,7],[20,0]]
        self.k2.connections[14] = [[0,0],LEFT]
        self.k2.connections[13] = [[20, 10], RIGHT]
        self.k2.connections[15] = [[20, 0], RIGHT]
        self.p = GraphWithConnection()
        self.p += Power('Пит.', highlight=highlight)
        self.p.labels += [5,6]
        self.p.labels_xy += [[0,0],[20,0]]
        self.p.connections[5] = [[0,0],LEFT]
        self.p.connections[6] = [[20, 0], RIGHT]
        self.vertices += [[0,0],[20,0],[20,-105],[0,-105],[0,0],[20,-102],[25,-102]]
        self.codes += [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.MOVETO,Path.LINETO]
        self.labels += ['ПС-3', name, 1,2,3,4]
        self.labels_xy += [[10,-4], [10,0],[2,-81],[2,-92],[2,-103],[18,-103]]
        k = ContactOpenClose('K1', highlight=highlight)
        k.mov_to(0,-30)
        self += k
        k = ContactOpenClose('K1', highlight=highlight)
        k.mov_to(0, -50)
        self += k
        k = ContactOpenClose('K2', highlight=highlight)
        k.mov_to(0, -70)
        self += k
        w= Power('Пит.', highlight=highlight)
        w.mov_to(0, -10)
        self +=w
        c = Capacitor('C1', highlight=highlight)
        c.mov_to(-11,-80)
        self += c
        c = Capacitor('C2', highlight=highlight)
        c.mov_to(-11, -91)
        self += c
        c = Capacitor('C3', highlight=highlight)
        c.mov_to(-11, -102)
        self += c
        g = Ground(highlight=highlight)
        g.mov_to(25,-102)
        self += g
        self.connections[8] = [[0,-30],self.k1,LEFT]
        self.connections[7] = [[20, -20], self.k1, RIGHT]
        self.connections[9] = [[20, -30], self.k1, RIGHT]
        self.connections[11] = [[0, -50], self.k1_1, LEFT]
        self.connections[12] = [[20, -40], self.k1_1, RIGHT]
        self.connections[10] = [[20, -50], self.k1_1, RIGHT]
        self.connections[14] = [[0, -70], self.k2, LEFT]
        self.connections[13] = [[20, -60], self.k2, RIGHT]
        self.connections[15] = [[20, -70], self.k2, RIGHT]
        self.connections[5] = [[0, -10], self.p, LEFT]
        self.connections[6] = [[20, -10], self.p, RIGHT]
        for key, value in self.connections.items():
            self.labels += [key]
            dx = 3 if value[0][0] == 0 else -3
            self.labels_xy += [[value[0][0]+dx,value[0][1]]]


class DUGA_O(GraphWithConnection):
    '''Регистратор дуговых замыканий ДУГА-О.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Регистратор дуговых замыканий ДУГА-О.'
        self.k1 = GraphWithConnection()
        self.k1 += ContactOpen(name+' Вых.1', highlight=highlight)
        self.k1.labels += [1, 2]
        self.k1.labels_xy += [[0, 0], [20, 0]]
        self.k1.connections[1] = [[0, 0], LEFT]
        self.k1.connections[2] = [[20, 0], RIGHT]
        self.k2 = GraphWithConnection()
        self.k2 += ContactOpen(name+' Вых.2', highlight=highlight)
        self.k2.labels += [3, 4]
        self.k2.labels_xy += [[0, 0], [20, 0]]
        self.k2.connections[3] = [[0, 0], LEFT]
        self.k2.connections[4] = [[20, 0], RIGHT]
        self.k3 = GraphWithConnection()
        self.k3 += ContactOpen(name+' Вых.3', highlight=highlight)
        self.k3.labels += [5, 6]
        self.k3.labels_xy += [[0, 0], [20, 0]]
        self.k3.connections[5] = [[0, 0], LEFT]
        self.k3.connections[6] = [[20, 0], RIGHT]
        self.k4 = GraphWithConnection()
        self.k4 += ContactOpen(name+' Вых.4', highlight=highlight)
        self.k4.labels += [7, 8]
        self.k4.labels_xy += [[0, 0], [20, 0]]
        self.k4.connections[7] = [[0, 0], LEFT]
        self.k4.connections[8] = [[20, 0], RIGHT]
        self.k5 = GraphWithConnection()
        self.k5 += ContactOpen(name+' Вых.5', highlight=highlight)
        self.k5.labels += [9, 10]
        self.k5.labels_xy += [[0, 0], [20, 0]]
        self.k5.connections[9] = [[0, 0], LEFT]
        self.k5.connections[10] = [[20, 0], RIGHT]
        self.k = GraphWithConnection()
        self.k += ContactClose(name + ' Отказ', highlight=highlight)
        self.k.labels += [9, 10]
        self.k.labels_xy += [[0, 0], [20, 0]]
        self.k.connections[11] = [[0, 0], LEFT]
        self.k.connections[12] = [[20, 0], RIGHT]
        self.w = GraphWithConnection()
        self.w += Power(name+' Uн', highlight=highlight)
        self.w.labels += [13, 14]
        self.w.labels_xy += [[0, 0], [20, 0]]
        self.w.connections[13] = [[0, 0], LEFT]
        self.w.connections[14] = [[20, 0], RIGHT]
        self.vertices += [[0, 1], [20, 1], [20, -77], [0, -77], [0, 1]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels += ['ДУГА-О', name, 'Вых.1','Вых.2','Вых.3','Вых.4','Вых.5','Отказ']
        self.labels_xy += [[10, -3], [10, 1],[8,-7],[9,-16],[9,-26],[9,-36],[9,-46],[10,-56]]
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -10)
        self += k
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -20)
        self += k
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -30)
        self += k
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -40)
        self += k
        k = ContactOpen(highlight=highlight)
        k.mov_to(0, -50)
        self += k
        k = ContactClose(highlight=highlight)
        k.mov_to(0, -60)
        self += k
        w = Power(name='220В',highlight=highlight)
        w.mov_to(0, -71)
        self += w
        self.connections[1] = [[0, -10], self.k1, LEFT]
        self.connections[2] = [[20, -10], self.k1, RIGHT]
        self.connections[3] = [[20, -20], self.k2, RIGHT]
        self.connections[4] = [[0, -20], self.k2, LEFT]
        self.connections[5] = [[20, -30], self.k3, RIGHT]
        self.connections[6] = [[20, -30], self.k3, RIGHT]
        self.connections[7] = [[0, -40], self.k4, LEFT]
        self.connections[8] = [[20, -40], self.k4, RIGHT]
        self.connections[9] = [[0, -50], self.k5, LEFT]
        self.connections[10] = [[20, -50], self.k5, RIGHT]
        self.connections[11] = [[0, -60], self.k, LEFT]
        self.connections[12] = [[20, -60], self.k, RIGHT]
        self.connections[13] = [[0, -70], self.w, LEFT]
        self.connections[14] = [[20, -70], self.w, RIGHT]
        for key, value in self.connections.items():
            self.labels += [key]
            dx = 3 if value[0][0] == 0 else -3
            self.labels_xy += [[value[0][0] + dx, value[0][1]]]


class PS12(GraphWithConnection):
    '''Панель сигнальная ПС-12 Сиинтез-Электро.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Панель сигнальная ПС-12 Сиинтез-Электро.'
        self.vertices += [[0, 0], [145, 0], [145, -20], [0, -20], [0, 0]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.l_bi = []
        for i in range(12):
            self.l_bi.append(GraphWithConnection(name, highlight=highlight))
            self.l_bi[-1] += BI('Вход ' + str(i + 1), highlight=highlight)
            self.l_bi[-1].labels += [name, str(i + 1)+'h', str(i + 1)]
            self.l_bi[-1].labels_xy += [[10, 2], [0, -2], [20, -2]]
            self.l_bi[-1].connections[str(i + 1)+'h'] = [[0, 0], LEFT]
            self.l_bi[-1].connections[str(i + 1)] = [[20, 0], RIGHT]
            self.connections[str(i + 1)+'h'] = [[i * 10 + 5, 0], self.l_bi[-1], UP]
            self.connections[str(i + 1)] = [[i * 10 + 5, -20], self.l_bi[-1], DOWN]
            self.labels += ['Вход' + str(i + 1), str(i + 1)+'h', str(i + 1)]
            self.labels_xy += [[i * 10 + 6, -12 if i%2 == 0 else -16], [i * 10 + 6, -4], [i * 10 + 6, -20]]
        self.p = GraphWithConnection(highlight=highlight)
        self.p += Power('Сеть', highlight=highlight)
        self.p.labels += [name, '14h', '14']
        self.p.labels_xy += [[10, 6], [0, 0], [20, 0]]
        self.p.connections['14h'] = [[0, 0], LEFT]
        self.p.connections['14'] = [[20, 0], RIGHT]
        self.connections['14h'] = [[140, 0], self.p, UP]
        self.connections['14'] = [[140, -20], self.p, DOWN]
        self.labels += ['Сеть', '14h', '14']
        self.labels_xy += [[140, -16], [140, -4], [140, -20]]
        self.r = GraphWithConnection()
        self.r += Power('Подсвет', highlight=highlight)
        self.r.labels += [name, '13h', '13']
        self.r.labels_xy += [[5, 6], [0, 0], [20, 0]]
        self.r.connections['13h'] = [[0, 0], LEFT]
        self.r.connections['13'] = [[20, 0], RIGHT]
        self.connections['13h'] = [[130, 0], self.r, UP]
        self.connections['13'] = [[130, -20], self.r, DOWN]
        self.labels += ['ПС-12', name, 'Подсвет', '13h', '13']
        self.labels_xy += [[70, -8], [70, 0], [130, -12], [130, -4], [130, -20]]


class C(GraphWithConnection):
    '''Конденсатор'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.c = GraphWithConnection()
        self.c += Capacitor(name=name, highlight=highlight)
        self.c.connections[1] = [[0,0],  LEFT]
        self.c.connections[2] = [[20, 0], RIGHT]
        self += Capacitor(name, highlight=highlight)
        self.connections[1] = [[0, 0], self.c, LEFT]
        self.connections[2] = [[15, 0], self.c, RIGHT]


class R3(GraphWithConnection):
    '''Реле R3N RELPOL'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.k1 = GraphWithConnection()
        self.k1 += ContactOpenClose(name,highlight=highlight)
        self.k1.labels += [11,12,14]
        self.k1.labels_xy += [[0,0],[20,7],[20,0]]
        self.k1.connections[11] = [[0,0],LEFT]
        self.k1.connections[12] = [[20, 10], RIGHT]
        self.k1.connections[14] = [[20, 0], RIGHT]
        self.k2 = GraphWithConnection()
        self.k2 += ContactOpenClose(name,highlight=highlight)
        self.k2.labels += [21,22,24]
        self.k2.labels_xy += [[0,0],[20,7],[20,0]]
        self.k2.connections[11] = [[0,0],LEFT]
        self.k2.connections[12] = [[20, 10], RIGHT]
        self.k2.connections[14] = [[20, 0], RIGHT]
        self.k3 = GraphWithConnection()
        self.k3 += ContactOpenClose(name,highlight=highlight)
        self.k3.labels += [31,32,34]
        self.k3.labels_xy += [[0,0],[20,7],[20,0]]
        self.k3.connections[11] = [[0,0],LEFT]
        self.k3.connections[12] = [[20, 10], RIGHT]
        self.k3.connections[14] = [[20, 0], RIGHT]
        self.w = GraphWithConnection()
        self.w += Winding(name, highlight=highlight)
        self.w.labels += ['A','B']
        self.w.labels_xy += [[0,0],[15,0]]
        self.w.connections['A'] = [[0,0],LEFT]
        self.w.connections['B'] = [[15, 0], RIGHT]
        self.vertices += [[0,0],[20,0],[20,-75],[0,-75],[0,0]]
        self.codes += [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO]
        self.labels += ['R3N', name]
        self.labels_xy += [[10,-4], [10,0]]
        k = ContactOpenClose(highlight=highlight)
        k.mov_to(0,-30)
        self += k
        k = ContactOpenClose(highlight=highlight)
        k.mov_to(0, -50)
        self += k
        k = ContactOpenClose(highlight=highlight)
        k.mov_to(0, -70)
        self += k
        w= Winding(highlight=highlight)
        w.mov_to(2.5,-10)
        self +=w
        self.connections[11] = [[0,-30],self.k1,LEFT]
        self.connections[12] = [[20, -20], self.k1, RIGHT]
        self.connections[14] = [[20, -30], self.k1, RIGHT]
        self.connections[21] = [[0, -50], self.k2, LEFT]
        self.connections[22] = [[20, -40], self.k2, RIGHT]
        self.connections[24] = [[20, -50], self.k2, RIGHT]
        self.connections[31] = [[0, -70], self.k3, LEFT]
        self.connections[32] = [[20, -60], self.k3, RIGHT]
        self.connections[34] = [[20, -70], self.k3, RIGHT]
        self.connections['A'] = [[0, -10], self.w, LEFT]
        self.connections['B'] = [[20, -10], self.w, RIGHT]
        for key, value in self.connections.items():
            self.labels += [key]
            dx = 3 if value[0][0] == 0 else -3
            self.labels_xy += [[value[0][0]+dx,value[0][1]]]


class CP8501_14(GraphWithConnection):
    '''Измерительный преобразователь ЦП8501/14 ООО “МНПП “Электроприбор”.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Измерительный преобразователь ЦП8501/14 ООО “МНПП “Электроприбор”.'
        self.vertices += [[0, 0], [80, 0], [80, -20], [0, -20], [0, 0]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.m = GraphWithConnection()
        self.m += Measurement('PA', highlight=highlight)
        self.m.connections[1] = [[0,0],LEFT]
        self.m.connections[2] = [[8, 0], RIGHT]
        self.p = GraphWithConnection(highlight=highlight)
        self.p += Power('Пит.', highlight=highlight)
        self.p.labels += [name, 4, 5]
        self.p.labels_xy += [[10, 6], [0, 0], [20, 0]]
        self.p.connections[4] = [[0, 0], LEFT]
        self.p.connections[5] = [[20, 0], RIGHT]
        self.o = GraphWithConnection(highlight=highlight)
        self.o += Power('Вых.', highlight=highlight)
        self.o.labels += [name, 13, 14]
        self.o.labels_xy += [[10, 6], [0, 0], [20, 0]]
        self.o.connections[13] = [[0, 0], LEFT]
        self.o.connections[14] = [[20, 0], RIGHT]
        self.connections[1] = [[5, -20], self.m, DOWN]
        self.connections[2] = [[15, -20], self.m, DOWN]
        self.connections[4] = [[35, -20], self.p, DOWN]
        self.connections[5] = [[45, -20], self.p, DOWN]
        self.connections[13] = [[65, -20], self.o, DOWN]
        self.connections[14] = [[75, -20], self.o, DOWN]
        self.labels += [self.name, 'ЦП8501/14','PA', 'Пит.', 'Вых.', 1,2,4,5,13,14]
        self.labels_xy += [[40,0], [40,-4],[10, -14], [40, -14], [70, -14],[5,-18],[15,-18],[35,-18],[45,-18],[65,-18],[75,-18]]


class CC301(GraphWithConnection):
    '''Счётчик электроэнергии СС-301.'''

    def __init__(self, name='', highlight=False):
        '''Конструктор класса СС301.'''
        super().__init__(name, highlight)
        self.type = 'Счётчик электроэнергии СС-301.'
        self.i = GraphWithConnection(highlight=highlight)
        self.i.vertices += [[0, 0], [25, 0], [25, -150], [0, -150], [0, 0]]
        self.i.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.i.connections[1] = [[0, -12], LEFT]
        self.i.connections[3] = [[25, -12], RIGHT]
        self.i.connections[4] = [[0, -37], LEFT]
        self.i.connections[6] = [[25, -37], RIGHT]
        self.i.connections[7] = [[0, -62], LEFT]
        self.i.connections[9] = [[25, -62], RIGHT]
        self.i.labels += [name, 1, 3, 4, 6, 7, 9]
        self.i.labels_xy += [[12, 5], [5, -14], [20, -14], [5, -39], [20, -39], [5, -64], [20, -64]]
        self.u = GraphWithConnection(highlight=highlight)
        self.u.vertices += [[0, 0], [25, 0], [25, -150], [0, -150], [0, 0]]
        self.u.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.u.connections[2] = [[0, -12], LEFT]
        self.u.connections[5] = [[25, -12], RIGHT]
        self.u.connections[8] = [[0, -37], LEFT]
        self.u.connections[10] = [[25, -37], RIGHT]
        self.u.connections[11] = [[0, -62], LEFT]
        self.u.labels += [name, 2, 5, 8, 10, 12]
        self.u.labels_xy += [[12, 5], [5, -14], [20, -14], [5, -39], [20, -39], [5, -64], [20, -64]]
        self.connections[1] = [[5, -15], self.i, DOWN]
        self.connections[2] = [[15, -15], self.u, DOWN]
        self.connections[3] = [[25, -15], self.i, DOWN]
        self.connections[4] = [[35, -15], self.i, DOWN]
        self.connections[5] = [[45, -15], self.u, DOWN]
        self.connections[6] = [[55, -15], self.i, DOWN]
        self.connections[7] = [[65, -15], self.i, DOWN]
        self.connections[8] = [[75, -15], self.u, DOWN]
        self.connections[9] = [[85, -15], self.i, DOWN]
        self.connections[10] = [[95, -15], self.u, DOWN]
        self.connections[11] = [[105, -15], self.u, DOWN]
        self.vertices += [[0,0],[110,0],[110,-15],[0,-15],[0,0]]
        self.codes += [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO]
        self.labels += [name, 'CC-301']
        self.labels_xy += [[55,0], [55,-5]]
        for key, value in self.connections.items():
            self.labels += [key]
            self.labels_xy += [[value[0][0],value[0][1]+1]]


class R(GraphWithConnection):
    '''Резистор'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.r = GraphWithConnection()
        self.r += Resistor(name=name, highlight=highlight)
        self.r.connections[1] = [[0,0], LEFT]
        self.r.connections[2] = [[20, 0], RIGHT]
        self += Resistor(name, highlight=highlight)
        self.connections[1] = [[0, 0], self.r, LEFT]
        self.connections[2] = [[15, 0], self.r, RIGHT]


class SB_F(GraphWithConnection):
    '''Кнопка управления с подсветкой ABLFS-22'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.k1 = GraphWithConnection()
        self.k1 += ButtonOpen(name, highlight=highlight)
        self.k1.connections[13] = [[0,0],LEFT]
        self.k1.connections[14] = [[20, 0], RIGHT]
        self.connections[13] = [[0,0],self.k1,LEFT]
        self.connections[14] = [[20, 0], self.k1, RIGHT]
        self.k2 = GraphWithConnection()
        self.k2 += ButtonClose(name, highlight=highlight)
        self.k2.connections[21] = [[0, 0], LEFT]
        self.k2.connections[22] = [[20, 0], RIGHT]
        self.connections[21] = [[0, -10], self.k2, LEFT]
        self.connections[22] = [[20, -10], self.k2, RIGHT]
        self.l = GraphWithConnection()
        self.l += Bulb(name, highlight=highlight)
        self.l.connections['X1'] = [[0, 0], LEFT]
        self.l.connections['X2'] = [[20, 0], RIGHT]
        self.connections['X1'] = [[0, -20], self.l, LEFT]
        self.connections['X2'] = [[20, -20], self.l, RIGHT]
        self.vertices += [[0,10],[20,10],[20,-25],[0,-25],[0,10]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self += ButtonOpen(highlight=highlight)
        b = ContactClose(highlight=highlight)
        b.mov_to(0,-10)
        self += b
        l = Bulb(highlight=highlight)
        l.mov_to(0,-20)
        self += l
        self.vertices += [[10,-11.5],[10,-10.5],[10,-9.5],[10,-8.5],[10, -7.5], [10, -6.5], [10, -5.5],
                          [10, -4.5],[10,-3.5],[10,-2.5],[10,-1.5],[10,-0.5],[10,0.5],[10,1.5]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.MOVETO,
                       Path.LINETO, Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]
        self.labels += [name, 13,14,21,22,'X1','X2']
        self.labels_xy += [[10,10],[2,0],[17,0],[2,-10],[17,-10],[2,-20],[17,-20]]


class SF(GraphWithConnection):
    '''Однополюсный автомат'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.k1_2 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name)
        k.rotate(90)
        k.labels_xy[0][0] += 10
        k.mov_to(0, -20)
        k.vertices += [[-1.5, -12], [-2.9, -12.7], [-4.6, -9.3], [-3.2, -8.6]]
        k.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.k1_2 += k
        self.k1_2.connections[1] = [[0, 0], UP]
        self.k1_2.connections[2] = [[0, -20], DOWN]
        self.k1_2.labels += [1, 2]
        self.k1_2.labels_xy += [[1, -2], [1, -22]]
        k = ContactOpen(name)
        k.rotate(90)
        k.labels_xy[0][0] += 10
        k.mov_to(0, -20)
        k.vertices += [[-1.5, -12], [-2.9, -12.7], [-4.6, -9.3], [-3.2, -8.6]]
        k.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self += k
        self.connections[1] = [[0, 0], self.k1_2, UP]
        self.connections[2] = [[0, -20], self.k1_2, DOWN]


class SF2(SF):
    '''Двухполюсный автомат'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.k3_4 = GraphWithConnection(highlight=highlight)
        k = ContactOpen(name)
        k.rotate(90)
        k.labels_xy[0][0] += 10
        k.mov_to(0, -20)
        k.vertices += [[-1.5, -12], [-2.9, -12.7], [-4.6, -9.3], [-3.2, -8.6]]
        k.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.k3_4 += k
        self.k3_4.connections[3] = [[0, 0], UP]
        self.k3_4.connections[4] = [[0, -20], DOWN]
        self.k3_4.labels += [3, 4]
        self.k3_4.labels_xy += [[1, -2], [1, -22]]
        k = ContactOpen(name)
        k.rotate(90)
        k.labels_xy[0][0] += 10
        k.mov_to(0, -20)
        k.vertices += [[-1.5, -12], [-2.9, -12.7], [-4.6, -9.3], [-3.2, -8.6]]
        k.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO]
        k.mov_to(20, 0)
        self += k
        self.connections[3] = [[20, 0], self.k3_4, UP]
        self.connections[4] = [[20, -20], self.k3_4, DOWN]


class BI4(GraphWithConnection):
    '''Блок испытательный БИ-4.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Блок испытательный БИ-4.'
        self.n = []
        for i in range(4):
            self.n.append(GraphWithConnection())
            self.n[-1] += ConnectionDetachable(name,highlight=highlight)
            self.n[-1].labels += [i*2+1,i*2+2]
            self.n[-1].labels_xy += [[-1,0],[3,0]]
            self.n[-1].connections[i*2+1] = [[0,0],LEFT]
            self.n[-1].connections[i * 2 + 2] = [[2, 0], RIGHT]
            c = ConnectionDetachable()
            c.rotate(90)
            c.mov_to(i*11+8, -13)
            self += c
            self.connections[i*2+1] = [[i * 11 +8,0], self.n[-1], UP]
            self.connections[i*2+2] = [[i * 11 +8,-20], self.n[-1], DOWN]
            self.labels += [i*2+1,i*2+2]
            self.labels_xy += [[i * 11 +8,-4],[i * 11 +8,-20]]
        self.vertices += [[0,0],[56,0],[56,-20],[0,-20],[0,0]]
        self.codes += [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO]
        self.labels += [name, 'БИ-4']
        self.labels_xy += [[-5,-12],[50,-4]]

class BI6(GraphWithConnection):
    '''Блок испытательный БИ-6.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Блок испытательный БИ-6.'
        self.n = []
        for i in range(6):
            self.n.append(GraphWithConnection())
            self.n[-1] += ConnectionDetachable(name, highlight=highlight)
            self.n[-1].labels += [i * 2 + 1, i * 2 + 2]
            self.n[-1].labels_xy += [[-1, 0], [3, 0]]
            self.n[-1].connections[i * 2 + 1] = [[0, 0], LEFT]
            self.n[-1].connections[i * 2 + 2] = [[2, 0], RIGHT]
            c = ConnectionDetachable()
            c.rotate(90)
            c.mov_to(i * 11 + 8, -13)
            self += c
            self.connections[i * 2 + 1] = [[i * 11 + 8, 0], self.n[-1], UP]
            self.connections[i * 2 + 2] = [[i * 11 + 8, -20], self.n[-1], DOWN]
            self.labels += [i * 2 + 1, i * 2 + 2]
            self.labels_xy += [[i * 11 + 8, -4], [i * 11 + 8, -20]]
        self.vertices += [[0, 0], [76, 0], [76, -20], [0, -20], [0, 0]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
        self.labels += [name, 'БИ-6']
        self.labels_xy += [[-5, -12], [71, -4]]

class AC22_old(GraphWithConnection):
    '''Переключатель AC22 старого образца.'''

    def __init__(self, name='', highlight=False):
        super().__init__(name, highlight=highlight)
        self.type = 'Переключатель AC22'
        self.k1 = GraphWithConnection()
        self.k1 += ContactOpen(name,highlight=highlight)
        self.k1.labels += [1,2]
        self.k1.labels_xy += [[0,0],[20,0]]
        self.k1.connections[1] = [[0,0],LEFT]
        self.k1.connections[2] = [[20, 0], RIGHT]
        self += ContactOpen(name,highlight=highlight)
        self.labels += [1, 2]
        self.labels_xy += [[2, 0], [18, 0]]
        self.connections[1] = [[0, 0], self.k1, LEFT]
        self.connections[2] = [[20, 0], self.k1, RIGHT]
        self.vertices += [[0, 6], [20, 6], [20, -3], [0, -3], [0, 6]]
        self.codes += [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]
