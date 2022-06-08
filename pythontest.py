import ifcopenshell
import ifcopenshell.geom

model = ifcopenshell.open("resources\Project 001.ifc")

walls = model.by_type("IfcWall")
beams = model.by_type("IfcBeam")

for beam in beams:
    print(beam.attribute_name)