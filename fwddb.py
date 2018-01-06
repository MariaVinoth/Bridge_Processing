
f_line_one = True
line_array1 = []
line_array2 = []
host = []
port = []
src_addr = []
destn_addr = []
in_port = []
src_has_entry = False
destn_has_entry = False
output_message = []
src_portno = 0
output_result = []
output_fdb = []
src_entry = []
destn_entry = []
src_entry_port = []
destn_entry_port = []

#reading first input file

with open("Input1.txt") as f1:
    for line in f1:
        if f_line_one == True:
            no_of_ports = line
            f_line_one = False
            
        else:
            line = filter(lambda x: not x.isspace(), line)
            line_array1.append(line)

 
inp1_ary_sz = len(line_array1)
for i in range(inp1_ary_sz):
    temp_string1 = line_array1[i]
    host.append(temp_string1[0])
    port.append(temp_string1[1])


#reading second input file


with open("Input2.txt") as f2:
    for line in f2:
        line = filter(lambda x: not x.isspace(), line)
        line_array2.append(line)


inp_len = len(line_array2)
for i in range(inp_len):
    temp_string2 = line_array2[i]
    src_addr.append(temp_string2[0])
    destn_addr.append(temp_string2[1])
    in_port.append(temp_string2[2])


#Accessing and updating the Forwarding Database and sending the packets to the correct destinations

def update_fdb(indx):
    host.append(src_addr[indx])
    port.append(in_port[indx])
    return (host, port)


host_len = len(host)

for i in range(inp_len):
    for j in range(len(host)):
        if(src_addr[i] == host[j]):
            src_has_entry = True
            src_portno = port[j]
            break
    for k in range(len(host)):
        if(destn_addr[i] == host[k]):
            destn_has_entry = True
            destn_portno = port[k]
            break            
    
    if src_has_entry:
        if destn_has_entry:
            if (src_portno == destn_portno):
                output_message.append("Frame discarded")
            else:
                output_message.append("Frame sent on port" +" "+destn_portno)
        else:
            output_message.append("Frame broadcast on all out ports")
    else:
        update_fdb(i)        
        if destn_has_entry:
            if(in_port[i] == destn_portno):
                output_message.append("FDB updated;Frame discarded")
            else:
                output_message.append("FDB updated;Frame sent on port" +" "+destn_portno)
        else:
            output_message.append("FDB updated;Frame broadcast on all out ports")
    src_has_entry = False
    destn_has_entry = False

    
    
    


#output

op_res = open("Output_result.txt","w")
op_res.write("The Output is\n")
op_res.write("\n")
for x in range(inp_len):
    op_res.write(src_addr[x] +" "+ destn_addr[x] +" "+ in_port[x]+ " " +output_message[x]+"\n")
op_res.write("\n")
op_res.write("\n")
op_res.write("The final FDB table is\n")
op_res.write("\n")
for y in range(len(host)):
    op_res.write(host[y] +" "+ port[y]+"\n")


op_res.close()    


