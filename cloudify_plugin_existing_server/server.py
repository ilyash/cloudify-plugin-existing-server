from cloudify.decorators import operation
from cloudify.manager import get_node_state, update_node_state

@operation
def start(ctx, **kwargs):
    node_state = get_node_state(node_id)
    node_state['management_ip'] = ctx.properties['ip']
    update_node_state(node_state)
    ctx.set_started()

@operation
def stop(ctx, **kwargs):
    ctx.set_stopped()