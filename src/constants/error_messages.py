class ErrorMessages:
    TOKEN_EXPIRED = "Token has expired"
    TOKEN_INVALID_CLAIMS = "Invalid token claims"
    TOKEN_INVALID = "Invalid or malformed token"
    TOKEN_GENERATION_FAILED = "Failed to generate token"
    TOKEN_UNKNOWN_ERROR = "Unknown token validation error"

    #Database operation
    DB_SESSION_MISSING = "Database session is missing"
    DB_OPERATION_FAILED = "Database Operation failed"
    
    
    # GENERAL ERRORS
    INTERNAL_SERVER_ERROR = "Internal server error"
   
    VALIDATION_ERROR = "Validation error"

    #roles

    ACESS_DENIED = "Access denied"
    # USER ERRORS
    USER_NOT_FOUND = "User not found"
    EMAIL_ALREADY_EXISTS = "Email is already registered"

    # AUTH / PASSWORD ERRORS
    INVALID_CREDENTIALS = "Invalid credentials"
    PASSWORD_TOO_SHORT = "Password must be at least 6 characters"
    PASSWORD_EMPTY = "Password cannot be empty"

    # NAME ERRORS
    NAME_EMPTY = "Name cannot be empty"
    NAME_ONLY_LETTERS = "Name must contain only letters"

    # DRONE ERRORS
    DRONE_NOT_FOUND = "Drone not found"
    DRONE_NAME_EMPTY = "Drone name cannot be empty"
    DRONE_NAME_ONLY_LETTERS = "Drone name must contain only letters"

    #mission
    MISSION_ALREADY_EXISTS = "Mission already exists"

    #Reports
    REPORT_ALREADY_EXISTS = "Report already exists"


