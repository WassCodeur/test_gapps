"""Module to manage fastapi models."""

from typing import List, Optional
from pydantic import BaseModel


class TimeZone(BaseModel):
    id: str
    offset: int


class CommonEvent(BaseModel):
    userLocale: Optional[str] = None
    hostApp: str
    platform: str
    timeZone: Optional[TimeZone] = None
    parameters: dict = {}
    formInputs: dict = {}


class AuthorizationEvent(BaseModel):
    userOAuthToken: str
    systemIdToken: str
    userIdToken: str


class DriveItem(BaseModel):
    id: Optional[str] = None
    iconUrl: Optional[str] = None
    mimeType: Optional[str] = None
    title: Optional[str] = None
    addonHasFileScopePermission: bool = False


class DriveEvent(BaseModel):
    selectedItems: List[DriveItem] = []
    activeCursorItem: Optional[DriveItem] = None


class EditorEvent(BaseModel):
    """Docs, Sheets, slides """
    id: Optional[str] = None
    title: Optional[str] = None
    addonHasFileScopePermission: bool = False


class GmailEvent(BaseModel):
    messageId: Optional[str] = None
    threadId: Optional[str] = None
    accessToken: Optional[str] = None
    toRecipients: List[str] = []
    ccRecipients: List[str] = []
    bccRecipients: List[str] = []


class Organizer(BaseModel):
    email: Optional[str] = None


class Capabilities(BaseModel):
    canSeeAttendees: Optional[bool] = None
    canAddAttendees: Optional[bool] = None
    canSeeConferenceData: Optional[bool] = None
    canSetConferenceData: Optional[bool] = None


class Attendee(BaseModel):
    email: Optional[str] = None
    optional: Optional[bool] = None
    displayName: Optional[str] = None
    organizer: Optional[bool] = None
    # self: Optional[bool] = None
    resource: Optional[bool] = None
    responseStatus: Optional[str] = None
    comment: Optional[str] = None
    additionalGuests: Optional[int] = None


class ConferenceSolution(BaseModel):
    iconUri: Optional[str] = None
    key: Optional[dict] = None
    name: Optional[str] = None


class EntryPoint(BaseModel):
    accessCode: Optional[str] = None
    entryPointFeatures: List[str] = None
    entryPointType: Optional[str] = None
    label: Optional[str] = None
    meetingCode: Optional[str] = None
    passcode: Optional[str] = None
    password: Optional[str] = None
    pin: Optional[str] = None
    regionCode: Optional[str] = None
    uri: Optional[str] = None


class ConferenceData(BaseModel):
    conferenceId: Optional[str] = None
    conferenceSolution: Optional[ConferenceSolution] = None
    entryPoints: List[EntryPoint] = None
    notes: Optional[str] = None
    parameters: Optional[dict] = None


class CalendarEvent(BaseModel):
    id: Optional[str] = None   # the event id
    recurringEventId: Optional[str] = None
    calendarId: Optional[str] = None
    organizer: Optional[Organizer] = None
    attendees: List[Attendee] = []
    conferenceData: Optional[ConferenceData ]= None
    capabilities: Optional[Capabilities] = None


class GEvent(BaseModel):
    commonEventObject: CommonEvent
    authorizationEventObject: AuthorizationEvent
    drive: Optional[DriveEvent] = None
    docs: Optional[EditorEvent] = None
    sheets: Optional[EditorEvent] = None
    slides: Optional[EditorEvent] = None
    gmail: Optional[GmailEvent] = None
    calendar: Optional[CalendarEvent] = None
