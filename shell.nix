{ pkgs ? import <nixpkgs> {} }:
let my-python-packages = p: with p; [
  pandas
  numpy
  pytest
  yapf
  pynvim
];
my-python = pkgs.python3.withPackages my-python-packages;
in my-python.env
