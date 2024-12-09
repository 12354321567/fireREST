from pydantic import BaseModel
from typing import List, Optional, Union, Dict

# Define nested models

class AccessPolicy(BaseModel):
    name: str
    id: str
    type: str

class Domain(BaseModel):
    name: str
    id: str
    type: str

class Metadata(BaseModel):
    ruleIndex: int
    section: str
    category: str
    accessPolicy: AccessPolicy
    timestamp: int
    domain: Domain

class Link(BaseModel):
    self: str

class TimeRange(BaseModel):
    name: str
    id: str
    type: str

class IPSPolicy(BaseModel):
    name: str
    id: str
    type: str
    inspectionMode: str

class NetworkObject(BaseModel):
    type: str
    overridable: bool
    id: str
    name: str

class NetworkObjectCountry(BaseModel):
    type: str
    id: str
    name: str

class DestinationNetworks(BaseModel):
    objects: List[NetworkObject | NetworkObjectCountry] = None

class PortObject(BaseModel):
    type: str
    protocol: str
    overridable: bool
    id: str
    name: str

class PortObjectGroup(BaseModel):
    type: str
    overridable: bool
    id: str
    name: str

class DestinationPorts(BaseModel):
    objects: List[PortObject | PortObjectGroup] = None

class SecurityZone(BaseModel):
    name: str
    id: str
    type: str
    subType: str

class FilePolicy(BaseModel):
    name: str
    id: str
    type: str

class VariableSet(BaseModel):
    name: str
    id: str
    type: str

class Application(BaseModel):
    id: str
    type: str
    name: str

class UrlObject(BaseModel):
    type: str
    overridable: bool
    id: str
    name: str

class URLCategory(BaseModel):
    name: str
    id: str
    type: str

class UrlCategoryWithReputation(BaseModel):
    reputation: str
    category: URLCategory
    type: str

class URLs(BaseModel):
    objects: List[UrlObject] = None
    urlCategoriesWithReputation: List[UrlCategoryWithReputation] = None

class Realm(BaseModel):
    id: str
    type: str
    name: str

class UserObject(BaseModel):
    id: str
    type: str
    name: str
    realm: Realm

# Main model
class AccessRuleResponse(BaseModel):
    metadata: Metadata
    links: Link
    timeRangeObjects: List[TimeRange] = None
    enabled: bool
    ipsPolicy: IPSPolicy = None
    sendEventsToFMC: bool
    destinationDynamicObjects: Dict[str, Optional[dict]]
    sourceNetworks: DestinationNetworks = None
    destinationNetworks: DestinationNetworks = None
    destinationPorts: DestinationPorts = None
    sourceZones: Dict[str, List[SecurityZone]] = None
    destinationZones: Dict[str, List[SecurityZone]] = None
    filePolicy: FilePolicy = None
    variableSet: VariableSet
    vlanTags: Dict[str, Optional[dict]]
    applications: Dict[str, List[Application]] = None
    urls: URLs = None
    logBegin: bool
    logEnd: bool
    logFiles: bool
    sourceDynamicObjects: Dict[str, Optional[dict]]
    enableSyslog: bool
    id: str
    users: Dict[str, List[UserObject]] = None
    action: str
    type: str
    name: str
