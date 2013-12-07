# revision 21338
# category Package
# catalog-ctan /macros/latex/contrib/karnaugh
# catalog-date 2007-01-08 14:40:40 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-karnaugh
Version:	20070108
Release:	5
Summary:	Typeset Karnaugh-Veitch-maps
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/karnaugh
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaugh.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaugh.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070108-2
+ Revision: 759947
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070108-1
+ Revision: 718767
- texlive-karnaugh
- texlive-karnaugh
- texlive-karnaugh
- texlive-karnaugh

