import os
import subprocess

from ayon_api import get_project
from ayon_core.pipeline import Anatomy
from ayon_ftrack.common import LocalAction
from ayon_ftrack.lib import get_ftrack_icon_url

import Acacia
from Acacia.lib.file_handler import toOSSep


class KickStartProject(LocalAction):
    "Action for kickstart project (katana)"

    # enabled = False

    identifier = 'lumine.kickstart.action'

    label = 'Initialize Katana'

    description = 'Initialize Action : generate template project for katana'

    priority = 10000

    role_list = ["Administrator", "Lead", "Supervisor"]

    icon = get_ftrack_icon_url("launch.png")

    # how to discover button action inside ftrack app
    def discover(self, session, entities, event):
        return self._discover_by_project(session, entities, event)

    def _discover_by_project(self, session, entities, event):
        # discover by its project name from entity type
        if (
            len(entities) != 1
            or entities[0].entity_type.lower() != "project"
        ):
            return False

        return True

    # action to do if launching button
    def launch(self, session, entities, event):
        # get project entity
        project_entity = self.get_project_from_entity(entities[0])
        # get project name from entity
        project_name = project_entity["full_name"]

        # get project doc
        project = get_project(project_name)

        # get anatomy from project name
        anatomy = Anatomy(project_name)

        # get acacia relative path from file import
        acacia_path = toOSSep(os.path.dirname(Acacia.__file__))

        # rough path fro kicktart.bat # refactor later
        bash_path = "{}/hosts/katana/scripts/project_kickstart.bat".format(
            acacia_path)

        # project root work from anatomy
        project_root = anatomy.roots["work"]

        # get project code from project data
        project_code = project["code"]

        bash_path = str(bash_path)
        acacia_path = str(acacia_path)
        project_root = str(project_root)
        project_code = str(project_code)

        # run subprocess args, than popen instead because need freeze section
        subprocess.run([bash_path, acacia_path, project_root, project_code])

        return True

# registering class


def register(session):
    KickStartProject(session).register()
