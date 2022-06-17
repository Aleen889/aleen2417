from OpenFlow import ofp_Packet_out
match = of.ofp_match()
match.in_port = 3
ofp_packet_out OpenFlow message
def send_packet (self, buffer_id, raw_data, out_port, in_port):
"""
Sends a packet out of the specified switch port.
If buffer_id is a valid buffer on the switch, use that.
Otherwise, send the raw data in raw_data.
The "in_port" is the port number that packet arrived on. Use
OFPP_NONE if you're generating this packet.
"""
msg = of.ofp_packet_out()
msg.in_port = in_port
if buffer_id != -1 and buffer_id is not None:
    msg.buffer_id = buffer_id
    else:
        if raw_data is None:
            return
            msg.data = raw_data
    action = of.ofp_action_output(port = out_port)
    msg.actions.append(action)
    self.connection.send(msg)
ofp_flow_mod OpenFlow message