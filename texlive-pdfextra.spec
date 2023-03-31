Name:		texlive-pdfextra
Version:	61719
Release:	2
Summary:	Extra PDF features for (Op)TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfextra
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfextra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfextra.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides extra PDF features for OpTeX (or in
limited form for plain LuaTeX and LuaLaTeX). As a minimalistic
format, OpTeX does not support "advanced" features of the PDF
file format in its base. This third party package aims to
provide them. Summary of supported features: insertion of
multimedia (audio, video, 3D), hyperlinks and other actions,
triggering events, transitions, attachments.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/optex/pdfextra
%{_texmfdistdir}/tex/luatex/pdfextra
%doc %{_texmfdistdir}/doc/optex/pdfextra

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
