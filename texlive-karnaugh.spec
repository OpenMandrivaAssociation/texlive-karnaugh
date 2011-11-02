Name:		texlive-karnaugh
Version:	20070108
Release:	1
Summary:	Typeset Karnaugh-Veitch-maps
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/karnaugh
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaugh.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaugh.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Macros intended for typesetting Karnaugh-Maps and Veitch-Charts
in a simple and user-friendly way. Karnaugh-Maps and Veitch-
Charts are used to display and simplify logic functions
"manually". These macros can typeset Karnaugh-Maps and Veitch-
Charts with up to ten variables (=1024 entries).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/karnaugh/kvmacros.tex
%doc %{_texmfdistdir}/doc/latex/karnaugh/kvdoc.pdf
%doc %{_texmfdistdir}/doc/latex/karnaugh/kvdoc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
