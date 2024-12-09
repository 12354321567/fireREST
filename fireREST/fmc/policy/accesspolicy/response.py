from pydantic import BaseModel
from typing import Optional

class LockingStatus(BaseModel):
    """
    status: str can be one of the following values: UNLOCKED, LOCKED
    """
    status: str

class User(BaseModel):
    name: str

class Domain(BaseModel):
    name: str
    id: str
    type: str

class Links(BaseModel):
    self: str

class MetadataPolicy(BaseModel):
    inherit: bool
    lockingStatus: LockingStatus
    timestamp: int
    lastUser: User
    domain: Domain

    @property
    def date(self) -> None:
        """
        TODO: Add date property to return the timestamp in a human readable format, something like: 2021-09-01 12:00:00
        """
        return None

class Rules(BaseModel):
    refType: str
    links: Links
    type: str

class SecurityIntelligence(BaseModel):
    id: str
    type: str
    links: Links

class IdentityPolicySetting(BaseModel):
    id: str
    type: str
    name: str

class PrefilterPolicySetting(BaseModel):
    id: str
    type: str
    name: str

class DefaultAction(BaseModel):
    """
    TODO: Action should be an Enum with the following values: ALLOW, BLOCK, TRUST, MONITOR, TRUST, LEARN, TRUST, TRUST, TRUST
    """
    sendEventsToFMC: bool
    logBegin: bool
    logEnd: bool
    enableSyslog: bool
    action: str
    type: str
    id: str

class AccessPolicyResponse(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    type: str
    metadata: MetadataPolicy
    links: Links
    rules: Rules
    securityIntelligence: Optional[SecurityIntelligence] = None
    identityPolicySetting: Optional[IdentityPolicySetting] = None
    prefilterPolicySetting: Optional[PrefilterPolicySetting] = None
    defaultAction: DefaultAction