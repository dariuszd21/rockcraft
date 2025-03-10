# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2023 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Rockcraft Service Factory."""

from dataclasses import dataclass
from typing import TYPE_CHECKING

from craft_application import ServiceFactory
from craft_application import services as base_services

from rockcraft import services


@dataclass
class RockcraftServiceFactory(ServiceFactory):
    """Rockcraft-specific Service Factory."""

    # pylint: disable=invalid-name

    # This is a Rockcraft-specific service for OCI image handling
    ImageClass: type[services.RockcraftImageService] = services.RockcraftImageService

    # These are overrides of default ServiceFactory services
    LifecycleClass: type[  # type: ignore[reportIncompatibleVariableOverride]
        services.RockcraftLifecycleService
    ] = services.RockcraftLifecycleService
    PackageClass: type[base_services.PackageService] = services.RockcraftPackageService
    ProviderClass: type[  # type: ignore[reportIncompatibleVariableOverride]
        services.RockcraftProviderService
    ] = services.RockcraftProviderService
    InitClass: type[  # type: ignore[reportIncompatibleVariableOverride]
        services.RockcraftInitService
    ] = services.RockcraftInitService
    RemoteBuildClass: type[  # type: ignore[reportIncompatibleVariableOverride]
        services.RockcraftRemoteBuildService
    ] = services.RockcraftRemoteBuildService

    if TYPE_CHECKING:
        image: services.RockcraftImageService = None  # type: ignore[assignment]
