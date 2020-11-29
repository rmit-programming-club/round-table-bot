{ pkgs ? import <nixpkgs> {} }:
let
  my-python-packages = python-packages: with python-packages; [
    (pkgs.python3.pkgs.callPackage (import ./discordpy.nix) {})
  ]; 
  python-with-my-packages = pkgs.python3.withPackages my-python-packages;
in
pkgs.mkShell {
  name = "datebotenv";
  buildInputs = [
    (import ./requirements.nix {pkgs=pkgs;}).interpreter
  ];
}
