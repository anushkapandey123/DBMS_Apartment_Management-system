# DELIMITER $$
# CREATE TRIGGER trig_resi
# BEFORE DELETE
# ON residents FOR EACH ROW
# BEGIN
# Insert into backup_record select * from residents where flat_no = old.flat_no;

# END $$
# DELIMITER ;