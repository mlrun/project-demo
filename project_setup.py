# Copyright 2025 Iguazio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import mlrun


def setup(project: mlrun.projects.MlrunProject) -> mlrun.projects.MlrunProject:
    project.set_function(
        name="prep-data",
        func="prep_data.py",
        kind="job",
        handler="prep_data",
    )

    project.set_function(
        name="gen-iris",
        func="gen_iris.py",
        kind="job",
        handler="iris_generator",
    )

    project.log_artifact(
        "data",
        target_path="https://s3.wasabisys.com/iguazio/data/iris/iris.data.raw.csv",
    )

    return project
