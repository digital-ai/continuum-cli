#########################################################################
# Copyright 2011 Cloud Sidekick
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#########################################################################

import catoclient.catocommand
from catoclient.param import Param

class ResubmitTaskInstance(catoclient.catocommand.CatoCommand):

    Description = 'Resubmit an Errored or Cancelled Task Instance, for another attempt at completion.  Only valid on Instances that ended with Error or were Cancelled.'
    API = 'resubmit_task_instance'
    Examples = '''
    cato-resubmit-task-instance -i 43667
'''
    Options = [Param(name='instance', short_name='i', long_name='instance',
                     optional=False, ptype='string',
                     doc='The Task Instance number.')]

    def main(self):
        results = self.call_api(self.API, ['instance'])
        print(results)
