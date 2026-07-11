%global tl_name karnaugh
%global tl_revision 21338

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typeset Karnaugh-Veitch-maps
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/karnaugh
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaugh.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/karnaugh.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros for typesetting Karnaugh-Maps and Veitch-
Charts in a simple and user-friendly way. Karnaugh-Maps and Veitch-
Charts are used to display and simplify logic functions "manually".
These macros can typeset Karnaugh-Maps and Veitch-Charts with up to ten
variables (=1024 entries).

