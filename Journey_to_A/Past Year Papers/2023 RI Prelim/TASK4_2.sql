SELECT 
    Member.Name, 
    Member.Gender, 
    FitnessRecord.Height, 
    FitnessRecord.Weight, 
    FitnessRecord.WorkoutDate 
FROM 
    Member
LEFT OUTER JOIN FitnessRecord 
    ON Member.MemberID = FitnessRecord.MemberID
INNER JOIN (
    SELECT MemberID, MAX(WorkoutDate) AS LatestWorkoutDate
    FROM FitnessRecord
    GROUP BY MemberID
) LatestRecord
    ON FitnessRecord.MemberID = LatestRecord.MemberID 
    AND FitnessRecord.WorkoutDate = LatestRecord.LatestWorkoutDate
ORDER BY 
    Member.Gender ASC, 
    Member.Name ASC;
