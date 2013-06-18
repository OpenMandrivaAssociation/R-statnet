%global packname  statnet
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.6
Release:          2
Summary:          Software tools for the Statistical Modeling of Network Data
Group:            Sciences/Mathematics
License:          GPL-3 + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-network R-ergm R-latentnet R-degreenet R-sna R-abind R-shapes R-tools R-utils 
Requires:         R-relevent R-networksis R-hergm 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-network R-ergm R-latentnet R-degreenet R-sna R-abind R-shapes R-tools R-utils
BuildRequires:    R-relevent R-networksis R-hergm 

%description
An integrated set of tools for the representation, visualization, analysis
and simulation of network data. For an introduction type:

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
