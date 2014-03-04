from cloudify.decorators import operation
from cloudify.manager import get_node_state, update_node_state

@operation
def start(ctx, **kwargs):
    node_state = get_node_state(ctx.node_id)
    node_state['management_ip'] = ctx.properties['ip']
    update_node_state(node_state)
    ctx['state'] = True

@operation
def stop(ctx, **kwargs):
    ctx['state'] = False

@operation
def get_state(ctx, **kwargs):
    return ctx.runtime_properties['state']
