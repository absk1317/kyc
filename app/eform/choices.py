from app.core.choices import COUNTRY_CODE_LIST, INDIA_CODE,INDIA_STATE_CODE_LIST

"""
PREFIX LIST
"""
MR = 1
MRS = 2
MISS = 3
DR = 4
PREFIX_LIST = (
	(MR, "Mr"),
	(MRS, "Mrs"),
	(MISS, "Miss"),
	(DR, "Dr"),
)

"""
GENDER LIST
"""
MALE = 1
FEMALE = 2
TRANSGENDER = 3

GENDER_LIST = (
	(MALE, "Male"),
	(FEMALE, "Female"),
	(TRANSGENDER, "Transgender"),
)

"""
MARITAl STATUS LIST
"""

MARRIED = 1
UNMARRIED = 2
OTHERS_MARITAL_STATE = 3

MARITAL_STATUS_LIST = (
	(MARRIED, "Married"),
	(UNMARRIED, "Unmarried"),
	(OTHERS_MARITAL_STATE, "Others"),
)

"""
RESIDENTIAL STATUS LIST
"""

RESIDENT_INDIVIDUAL = 1
NON_RESIDENT_INDIVIDUAL = 2
FORIEGN_NATIONAL = 3
PERSON_OF_INDIAN_ORIGIN = 4

RESIDENTIAL_STATUS_LIST = (
	(RESIDENT_INDIVIDUAL, "Resident Individual"),
	(NON_RESIDENT_INDIVIDUAL, "Non Resident Individual"),
	(FORIEGN_NATIONAL, "Foriegn National"),
	(PERSON_OF_INDIAN_ORIGIN, "Person Of Indian Origin"),
)

"""
OCCUPATION TYPE LIST
"""

SERVICES = 1
PRIVATE_SECTOR = 2
PUBLIC_SECTOR = 3
GOVERNMENT_SECTOR = 4
PROFESSIONAL = 5
SELF_EMPLOYEED = 6
RETIRED = 7
HOUSE_WIFE = 8
STUDENT = 9
BUSINESS = 10
OTHER_OCCUPATION = 11
NOT_CATEGORISED = 12

OCCUPATION_TYPE_LIST = (
	(SERVICES, "Services"),
	(PRIVATE_SECTOR, "Private Sector"),
	(PUBLIC_SECTOR, "Public Sector"),
	(GOVERNMENT_SECTOR, "Government Sector"),
	(PROFESSIONAL, "Professional"),
	(SELF_EMPLOYEED, "Self Employeed"),
	(RETIRED, "Retired"),
	(HOUSE_WIFE, "House Wife"),
	(STUDENT, "Student"),
	(BUSINESS, "Business"),
	(OTHER_OCCUPATION, "Others"),
	(NOT_CATEGORISED, "Not Categorised"),

)

"""
POI TYPE LIST
"""
PASSPORT = 1 
VOTERS_ID = 2
DRIVING_LICENSE = 3
AADHAAR = 4
NREGA = 5
OTHER_POI = 6

POI_TYPE_LIST = (
	(PASSPORT, "Passport"),
	(VOTERS_ID, "Voters Id"),
	(DRIVING_LICENSE, "Driving License"),
	(AADHAAR, "Aadhaar"),
	(NREGA, "Nrega Job Card"),
	(OTHER_POI, "Others"),
)

"""
POA TYPE LIST
"""

POA_TYPE_LIST = (
	(PASSPORT, "Passport"),
	(VOTERS_ID, "Voters Id"),
	(DRIVING_LICENSE, "Driving License"),
	(AADHAAR, "Aadhaar"),
	(NREGA, "Nrega Job Card"),
	(OTHER_POI, "Others"),
)


"""
Address TYPE LIST

"""

RESIDENCE = 1 
BUSINESS = 2
REGISTERED_OFFICE = 3
RESIDENCE_BUSINESS = 4
UNSPECIFIED = 5

ADDRESS_TYPE_LIST = (
	(RESIDENCE, "Residence"),
	(BUSINESS, "Business"),
	(REGISTERED_OFFICE, "Registered Office"),
	(RESIDENCE_BUSINESS, "Residence / Business"),
	(UNSPECIFIED, "Unspecified"),
)

"""
Related Person TYPE LIST

"""
GUARDIAN = 1 
ASSIGNEE = 2
AUTHORIZED_REPRESENTATIVE = 3


RELATED_PERSON_TYPE_LIST = (
	(GUARDIAN, "Guardian"),
	(ASSIGNEE, "Assignee"),
	(AUTHORIZED_REPRESENTATIVE, "Authorized Representative"),
)

"""
APPLICATION STATE LIST

"""

APPLICATION_IN_PROGRESS = 1
APPLICATION_REJECTED  = 2
APPLICATION_SUCCESS = 3

APPLICATION_STATES_LIST = (
	(APPLICATION_IN_PROGRESS, "In Progress"),
	(APPLICATION_REJECTED, "Rejected"),
	(APPLICATION_SUCCESS, "Success"),
)







