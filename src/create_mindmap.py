from mekk.xmind import XMindDocument

OUTPUT = "test.xmind"

file_name = "SQL Test"
parent = ["Parent1", "Parent1", "Parent1", "Parent2", "Parent2", "Parent3", "Parent3", "Parent3", "Parent3", "Parent4", "Parent4"]
child = ["Child1", "Child2", "Child3", "Child4", "Child5", "Child6", "Child7", "Child8", "Child8", "Child10", "Child11"]
    
xmind = XMindDocument.create(file_name, file_name)
first_sheet = xmind.get_first_sheet()
root_topic = first_sheet.get_root_topic()

child_index = 0
parent_node = 0
for index, function in enumerate(parent, start=0):  # default is zero
    if index == 0:
        parent_node = root_topic.add_subtopic(function)
        child_node = parent_node.add_subtopic(child[child_index])
        child_index += 1
    else:
        if parent[index] == parent[index-1]:
            parent_node.add_subtopic(child[child_index])
            child_index += 1
        else:
            parent_node = root_topic.add_subtopic(function)
            child_node = parent_node.add_subtopic(child[child_index])
            child_index += 1

xmind.save(OUTPUT)
print ("Saved to", OUTPUT)



##EXAMPLE CODE FROM THE ONLINE SOURCE


##root_topic.add_subtopic(u"Detached topic", detached = True)
##t.add_subtopic(u"Another detached", detached = True)
##t.add_marker("flag-red")
##root_topic.add_subtopic(u"Link example").set_link("http://mekk.waw.pl")
##root_topic.add_subtopic(u"Attachment example").set_attachment(
##    file("test.sql").read(), ".txt")
##root_topic.add_subtopic(u"With note").set_note(u"""This is just some dummy note.""")

#MARKER_CODE = "40g6170ftul9bo17p1r31nqk2a"
#XMP = "../../py_mekk_nozbe2xmind/src/mekk/nozbe2xmind/NozbeIconsMarkerPackage.xmp"
#root_topic.add_subtopic(u"With non-standard marker").add_marker(MARKER_CODE)

#xmind.embed_markers(XMP)
#xmind.pretty_print()


