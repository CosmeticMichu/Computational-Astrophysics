SELECT COUNT(s.specobjid) as 'QSO objects total'
FROM PhotoObj AS P
JOIN SpecObj AS s ON p.objid = s.bestobjid
WHERE
    p.ra BETWEEN 130.9 AND 131.0
    AND p.g > 20.0
    AND s.z BETWEEN 0.2 AND 0.5
    AND s.class = 'QSO'