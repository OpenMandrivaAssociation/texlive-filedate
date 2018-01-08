# revision 29529
# category Package
# catalog-ctan /macros/latex/contrib/filedate
# catalog-date 2012-11-14 11:01:29 +0100
# catalog-license lppl
# catalog-version 0.4
Name:		texlive-filedate
Version:	20170414
Release:	1
Summary:	Access and compare info and modification dates
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/filedate
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filedate.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filedate.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/filedate.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
