table 1:
	-proc_name.id
	-proc. name
	-doc_id
	-original_graph
	-accuracy
	-extracted_at
	-edited_graph
	-last_edit_at
	-status (original/edited)

-----------
editing:
- in frontend: save the edited graph: 
	-"confirm changes": save the editions.
	- convert mermaid to json
	- validate the json format
- in backend: 
	- save the new graph in edited_graph
	- insert last edited time
	- change the status to edited 
--------
reading(display procedure graph):
	- if status is edited it should show edited graph by default.
	- (optional) there should be a option to show original graph.(switch between original and edited) 

 info to show about procedure graph:
	procedure name
	status: original/edited
	extract from (document name)
	accuracy of original graph
	extracted on(date/time)
	last edit (date/time)
	
	
