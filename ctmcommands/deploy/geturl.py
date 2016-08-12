#########################################################################
# 
# Copyright 2016 VersionOne
# All Rights Reserved.
# http://www.versionone.com
# 
# 
#########################################################################

import ctmcommands.cmd
from ctmcommands.param import Param


class GetURL(ctmcommands.cmd.CSKCommand):

    Description = 'Gets a URL to a specific page in the "deploy" UI.'
    API = 'get_maestro_url'
    Examples = ''''''
    Options = [Param(name='page', short_name='p', long_name='page',
                     optional=False, ptype='string',
                     doc='Name of a detail page. Valid values: deployment, service, service_instance, sequence_status, task_instance.'),
               Param(name='user', short_name='u', long_name='user',
                     optional=True, ptype='string',
                     doc='Value can be either a User ID or Name.'),
               Param(name='deployment', short_name='d', long_name='deployment',
                     optional=True, ptype='string',
                     doc='Value can be either a Deployment ID or Name.'),
               Param(name='service', short_name='v', long_name='service',
                     optional=True, ptype='string',
                     doc='Value can be either a Service ID or Name.'),
               Param(name='service_instance', short_name='i', long_name='service_instance',
                     optional=True, ptype='string',
                     doc='Value can be either a Service Instance ID or Name.'),
               Param(name='task_instance', short_name='t', long_name='task_instance',
                     optional=True, ptype='string',
                     doc='A Task Instance ID.'),
               Param(name='sequence_instance', short_name='s', long_name='sequence_instance',
                     optional=True, ptype='string',
                     doc='A Sequence Instance ID.')]

    def main(self):
        results = self.call_api(self.API, ['page', 'user', 'deployment', 'service', 'task_instance', 'service_instance', 'sequence_instance'])
        print(results)
