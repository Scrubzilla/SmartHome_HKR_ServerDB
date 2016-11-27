-- Stored Procedure for checking if an account exists and matches with the password that the user typed in.

-- Return values
-- 0 -> OK
-- 1 -> FAIL

CREATE PROCEDURE CheckLogin
  @username varchar(24) = null,
  @password varchar(32) = null

AS
  BEGIN

  -- If username and password exists return OK
  IF (SELECT * FROM [users] WHERE username = @username AND password = @password)
    return 0;

    END


  ELSE

    BEGIN
    return 1;
    END

