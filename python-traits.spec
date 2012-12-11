%define module	traits
%define name	python-%{module}
%define version	4.2.0
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release	%{rel}
%endif

Summary:	Enthought Tool Suite - explicitly typed attributes for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/traits/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	python-enthought-traits-ui
Obsoletes:	python-enthought-traits
Requires:	python-numpy >= 1.1.0
BuildRequires:	python-setupdocs >= 1.0.5
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	python-sphinx
%py_requires -d

%description
The Traits project allows Python programmers to use a special kind of type
definition called a trait which provides object attributes with some 
additional characteristics:

* Initialization: A trait has a default value, which is automatically
  set as the initial value of an attribute before its first use in a
  program.
* Validation: A trait attribute's type is explicitly declared. The
  type is evident in the code, and only values that meet a
  programmer-specified set of criteria (i.e., the trait definition)
  can be assigned to that attribute.
* Delegation: The value of a trait attribute can be contained either
  in the defining object or in another object delegated to by the
  trait.
* Notification: Setting the value of a trait attribute can notify
  other parts of the program that the value has changed.
* Visualization: User interfaces that allow a user to interactively
  modify the value of a trait attribute can be automatically
  constructed using the trait's definition. (This feature requires
  that a supported GUI toolkit be installed. If this feature is not
  used, the Traits project does not otherwise require GUI support.)

A class can freely mix trait-based attributes with normal Python
attributes, or can opt to allow the use of only a fixed or open set of
trait attributes within the class. Trait attributes defined by a class
are automatically inherited by any subclass derived from the class.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build
export PYTHONPATH=`ls -1d build/lib.* | head -1`
%__python setup.py build_docs --formats html

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc *.txt *.rst examples/ build/docs/html/
%py_platsitedir/%{module}*


%changelog
* Mon Aug 13 2012 Lev Givon <lev@mandriva.org> 4.2.0-1
+ Revision: 814679
- Update to 4.2.0.

* Tue Dec 27 2011 Lev Givon <lev@mandriva.org> 4.1.0-1
+ Revision: 745658
- Update to 4.1.0.

* Thu Jul 07 2011 Lev Givon <lev@mandriva.org> 4.0.0-1
+ Revision: 689158
- import python-traits


