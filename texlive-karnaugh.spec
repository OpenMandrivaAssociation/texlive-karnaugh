Name:		texlive-karnaugh
Version:	21338
Release:	2
Summary:	Typeset Karnaugh-Veitch-maps
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/karnaugh
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaugh.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaugh.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Macros intended for typesetting Karnaugh-Maps and Veitch-Charts
in a simple and user-friendly way. Karnaugh-Maps and Veitch-
Charts are used to display and simplify logic functions
"manually". These macros can typeset Karnaugh-Maps and Veitch-
Charts with up to ten variables (=1024 entries).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/karnaugh/kvmacros.tex
%doc %{_texmfdistdir}/doc/latex/karnaugh/kvdoc.pdf
%doc %{_texmfdistdir}/doc/latex/karnaugh/kvdoc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
