SELECT
p.objid, s.class, s.z AS redshift, p.i, p.z

FROM PhotoObj AS p
JOIN SpecObj AS s ON p.objid = s.bestobjid 
WHERE 
    p.ra BETWEEN 130.9 AND 131.0
    AND p.g > 20.0
    AND s.z BETWEEN 0.2 AND 0.5
    AND s.class = 'QSO'
    
ORDER BY s.z ASC