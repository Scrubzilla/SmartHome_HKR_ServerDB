-- Stored Procedure for checking if a new users, username and email is avaible

-- Return values
-- 0 -> OK
-- 1 -> FAIL (Either the username or email is already taken)

CREATE PROCEDURE NewUser
  @username varchar(24) = null,
  @password varchar(32) = null,
  @email varchar(40) = null

  AS


  -- If the username or email already exists, return FAIL
  IF EXISTS(SELECT * FROM [users] WHERE username = @username OR email = @email)
     BEGIN

      RETURN 1

      END

    -- Else insert the given values into the database and return OK
    ELSE

      BEGIN

      INSERT INTO [dbo].[users] (Username, User_password, Email)
      VALUES (@username, @password, @email)

      RETURN  0

      END


