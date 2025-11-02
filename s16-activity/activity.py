import ifcopenshell
ifc_file = ifcopenshell.open("AC20-FZK-Haus.ifc")

# 3_____________________________________________________
print("IFC file loaded:", ifc_file.schema)

# 4_____________________________________________________
project = ifc_file.by_type("IfcProject")[0] 
project_name = project.Name or "Unnamed Project"
print(f"Project: {project_name}")

# 5_____________________________________________________
stairs = ifc_file.by_type("IFCStair")
print(f"Number of Stairs: {len(stairs)}")
for stair in stairs:
	print(stair.GlobalId, stair.Name)

# 6_____________________________________________________
slabs = ifc_file.by_type("IFCSlab")
print(f"Number of Slabs: {len(slabs)}")
for slab in slabs:
	print(slab.GlobalId, slab.Name)

# 7_____________________________________________________
slabs = ifc_file.by_type("IFCSlab")
for i, slab in enumerate(slabs, 1):
	slab.Name = f"Renamed_Slab{i}"
	print(f"Updated Slab: {slab.GlobalId} → {slab.Name}")

# 8_____________________________________________________
project = ifc_file.by_type("IFCProject")[0]
for site in project.IsDecomposedBy[0].RelatedObjects:
	for building in site.IsDecomposedBy[0].RelatedObjects:
		for storey in building.IsDecomposedBy[0].RelatedObjects:
			print("Storey", storey.Name, "Elevation", storey.Elevation)

# 9_____________________________________________________
types = set(el.is_a() for el in ifc_file)
print("Object Types in File", types)

# 10_____________________________________________________
ifc_file.write("AC20-FZK-Haus_Renamed.ifc")
