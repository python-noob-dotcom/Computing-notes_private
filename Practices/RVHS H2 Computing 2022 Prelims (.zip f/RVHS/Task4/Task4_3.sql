SELECT SubjectName, PaperNo, Role, VenueName, Date, StartTime, EndTime
FROM Teacher, Venue, ExamSession, ExamDuty
WHERE Teacher.TeacherID = ExamDuty.TeacherID
AND ExamSession.ExamSessionID = ExamDuty.ExamSessionID
AND ExamSession.VenueID = Venue.VenueID
AND Name = "Marissa Partridge"
ORDER BY "Date" ASC, StartTime ASC