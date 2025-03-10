#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Type hints for NumPy
Summary(pl.UTF-8):	Podpowiedzi typów dla NumPy
Name:		python3-nptyping
Version:	2.5.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/nptyping/
Source0:	https://files.pythonhosted.org/packages/source/n/nptyping/nptyping-%{version}.tar.gz
# Source0-md5:	08bddbff6a31f7e42d59ec1d4819d0e5
URL:		https://pypi.org/project/nptyping/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
#TODO: beartype>=0.10.0 (for 3.10+), mypy, pyright, typeguard
BuildRequires:	python3-feedparser
BuildRequires:	python3-invoke >= 1.6.0
BuildRequires:	python3-numpy >= 1.20.0
BuildRequires:	python3-pandas
BuildRequires:	python3-typing_extensions >= 4
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
- type hints for NumPy
- type hints for pandas.DataFrame
- extensive dynamic type checks for dtypes shapes and structures

%description -l pl.UTF-8
- podpowiedzi typów dla NumPy
- podpowiedzi typów dla pandas.DataFrame
- rozszerzone dynamiczne sprawdzanie typów dla form i struktur dtype

%prep
%setup -q -n nptyping-%{version}

# requires beartype (TODO)
%{__rm} tests/test_beartype.py
# requires mypy (TODO)
%{__rm} tests/test_mypy.py tests/pandas_/test_mypy_dataframe.py
# for author (before release)
%{__rm} tests/test_package_info.py
# requires pyright (TODO)
%{__rm} tests/test_pyright.py
# pip manipulation
%{__rm} tests/test_wheel.py
# requires typeguard (TODO)
%{__rm} tests/test_typeguard.py
# no pandas 1.5.x in PLD yet
%{__rm} tests/pandas_/test_fork_sync.py
# requires mypy (TODO)
%{__rm} tests/test_helpers/check_mypy_on_code.py

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY.md LICENSE README.md USERDOCS.md
%{py3_sitescriptdir}/nptyping
%{py3_sitescriptdir}/nptyping-%{version}-py*.egg-info
