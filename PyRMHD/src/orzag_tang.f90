!=======================================================================
!  Implements the ORZAG-TANG VORTEX test
!=======================================================================
module OrzagTang
  use parameters
  implicit none
  real :: rho, vx, vy, vz, p
  real :: Bx, By, Bz
contains

  subroutine init_ot()
    implicit none
    
    rho = 25./9.
    p   = 5./3.
    
  end subroutine init_ot

  !--------------------------------------------------------------------
  ! Initial conditions for the BRIO-WU shock tube
  subroutine impose_ot(u)
    use globals, only : coords, dx, dy
    use parameters, only : nxtot
    implicit none
    real, intent(out) :: u(neq,nxmin:nxmax,nymin:nymax,nzmin:nzmax)
    real :: x, y
    integer ::  i,j,k

    do i=nxmin,nxmax
       do j=nymin,nymax
          do k=nzmin,nzmax

             ! Position measured from the bottom corner of the grid
             x=(float(i+coords(0)*nx)+0.5)*dx !WHY +0.5?
             y=(float(i+coords(1)*ny)+0.5)*dy !WHY +0.5?

                vx = -sin(y )
                vy =  sin(y )
                vz = 0.
                bx = -sin(y )
                by =  sin(2*x)
                bz = 0.
                              

                !   total density and momena
                u(1,i,j,k) = rho
                u(2,i,j,k) = rho*vx
                u(3,i,j,k) = rho*vy
                u(4,i,j,k) = rho*vz
                !   total energy
                u(5,i,j,k)=0.5*rho*(vx**2+vy**2+vz**2)+cv*p  &
                               +0.5*(Bx**2+By**2+Bz**2)
                u(6,i,j,k) =  Bx
                u(7,i,j,k) =  By
                u(8,i,j,k) =  BZ

          end do
       end do
    end do

  end subroutine impose_ot
  !--------------------------------------------------------------------

end module OrzagTang
