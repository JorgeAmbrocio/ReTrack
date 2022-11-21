-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema retrack
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `retrack` ;

-- -----------------------------------------------------
-- Schema retrack
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `retrack` DEFAULT CHARACTER SET utf8 ;
USE `retrack` ;

-- -----------------------------------------------------
-- Table `retrack`.`Tienda`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `retrack`.`Tienda` ;

CREATE TABLE IF NOT EXISTS `retrack`.`Tienda` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `retrack`.`Piso`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `retrack`.`Piso` ;

CREATE TABLE IF NOT EXISTS `retrack`.`Piso` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `idTienda` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Piso_Tienda_idx` (`idTienda` ASC) VISIBLE,
  CONSTRAINT `fk_Piso_Tienda`
    FOREIGN KEY (`idTienda`)
    REFERENCES `retrack`.`Tienda` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `retrack`.`Direccion`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `retrack`.`Direccion` ;

CREATE TABLE IF NOT EXISTS `retrack`.`Direccion` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `retrack`.`Pasillo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `retrack`.`Pasillo` ;

CREATE TABLE IF NOT EXISTS `retrack`.`Pasillo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `cntSecciones` VARCHAR(45) NULL,
  `puntosLimitadores` VARCHAR(45) NULL,
  `idDireccion` INT NOT NULL,
  `idPiso` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Pasillo_Direccion1_idx` (`idDireccion` ASC) VISIBLE,
  INDEX `fk_Pasillo_Piso1_idx` (`idPiso` ASC) VISIBLE,
  CONSTRAINT `fk_Pasillo_Direccion1`
    FOREIGN KEY (`idDireccion`)
    REFERENCES `retrack`.`Direccion` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Pasillo_Piso1`
    FOREIGN KEY (`idPiso`)
    REFERENCES `retrack`.`Piso` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
