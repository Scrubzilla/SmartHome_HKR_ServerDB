-- Stored Procedure for checking if an account exists and matches with the password that the user typed in.

-- Return values
-- 0 -> OK
-- 1 -> FAIL

CREATE PROCEDURE CheckLogin
  @username varchar(24) = null,
  @password varchar(32) = null

AS

  -- If username and password exists return OK
  IF EXISTS(SELECT * FROM [users] WHERE username = @username AND user_password = @password)

    BEGIN

    RETURN 0

    END




  ELSE

    BEGIN

    RETURN 1

    END

