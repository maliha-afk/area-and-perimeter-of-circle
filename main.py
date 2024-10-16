class circle:
    def __init__(self,perimeter,area,have_radius,have_middlepoint):
        self.perimeter=perimeter
        self.area=area
        self.have_radius=have_radius
        self.have_middlepoint=have_middlepoint


circle1=circle(31.42,78.54,True,True)

square=circle(False,20,False,False)

print(circle1.perimeter)
print(square.perimeter)

