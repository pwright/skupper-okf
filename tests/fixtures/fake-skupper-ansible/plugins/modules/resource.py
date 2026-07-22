DOCUMENTATION = r'''
---
module: resource
short_description: Place Skupper resources
version_added: "2.0.0"
description:
  - Applies Skupper resource definitions.
options:
  path:
    description:
      - Path to resource definitions.
    type: str
  state:
    description:
      - Resource state.
    type: str
    default: present
    choices: ["present", "absent"]
extends_documentation_fragment:
  - skupper.v2.common_options
requirements:
  - "python >= 3.9"
'''

EXAMPLES = r'''
- name: Apply resources
  skupper.v2.resource:
    path: ./resources
    namespace: west
'''

RETURN = r'''
changed:
  description:
    - Whether anything changed.
  type: bool
'''
