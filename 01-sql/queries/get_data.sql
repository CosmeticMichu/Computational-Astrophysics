--This query has to be executed in the SQL Search section of the SkyService SDSS website
--(http://cas.sdss.org/dr18/SearchTools/checkQuery) in order to retrieve the astrphysical data.
SELECT
p.objid, p.ra, p.dec, p.u, p.g, p.r, p.i, p.z,
s.specobjid, s.class, s.z as redshift

FROM PhotoObj AS p
JOIN SpecObj AS s ON p.objid = s.bestobjid 
WHERE 
    p.ra BETWEEN 130.9 AND 131.0
    AND p.g > 20.0
    AND s.z BETWEEN 0.2 AND 0.5