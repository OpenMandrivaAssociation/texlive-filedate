Name:		texlive-filedate
Version:	29529
Release:	2
Summary:	Access and compare info and modification dates
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/filedate
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filedate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filedate.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filedate.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides basic access to the date of a LaTeX source
file according to its \Provides... entry (the "info date") as
well as to its modification date according to \pdffilemoddate
if the latter is available.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/filedate/filedate.RLS
%{_texmfdistdir}/tex/latex/filedate/filedate.sty
%doc %{_texmfdistdir}/doc/latex/filedate/Announce.txt
%doc %{_texmfdistdir}/doc/latex/filedate/README
%doc %{_texmfdistdir}/doc/latex/filedate/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/latex/filedate/filedate.pdf
#- source
%doc %{_texmfdistdir}/source/latex/filedate/fdatechk.tex
%doc %{_texmfdistdir}/source/latex/filedate/filedate.tex
%doc %{_texmfdistdir}/source/latex/filedate/srcfiles.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
