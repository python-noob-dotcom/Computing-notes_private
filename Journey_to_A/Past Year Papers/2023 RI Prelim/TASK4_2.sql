SELECT COUNT(DISTINCT(Member.MemberID)), ROUND(AVG(Member.Age), 1) , ROUND(AVG(Weight), 1), ROUND(AVG(Height), 1)
FROM Member LEFT OUTER JOIN 
    
    (FitnessRecord
INNER JOIN (
    SELECT MemberID, MAX(WorkoutDate) AS LatestWorkoutDate
    FROM FitnessRecord
    GROUP BY MemberID
) LatestRecord
    ON FitnessRecord.MemberID = LatestRecord.MemberID 
    AND FitnessRecord.WorkoutDate = LatestRecord.LatestWorkoutDate) AS A

    ON Member.MemberID = A.MemberID