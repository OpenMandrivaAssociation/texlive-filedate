%global tl_name filedate
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Access and compare info and modification dates
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/filedate
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/filedate.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/filedate.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/filedate.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides basic access to the date of a LaTeX source file
according to its \Provides... entry (the "info date") as well as to its
modification date according to \pdffilemoddate if the latter is
available.

